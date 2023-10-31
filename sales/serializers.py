from rest_framework import serializers

from sales.models import Company, Contacts, Product


class ContactsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Product
        fields = ('id', 'title', 'model')


class CompanySerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(many=True, required=True)
    product = ProductSerializer(many=True, required=False)

    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        if 'product' in self.initial_data:
            products_data = validated_data.pop('product')
        contacts_data = validated_data.pop('contacts')
        company = Company.objects.create(**validated_data)

        if 'product' in self.initial_data:
            for product in products_data:
                Product.objects.create(company=company, **product)

        for contact in contacts_data:
            Contacts.objects.create(company=company, **contact)

        return company


class CompanyUpdateSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(many=True, required=False)
    product = ProductSerializer(many=True, required=False)

    class Meta:
        model = Company
        exclude = ('debt',)

    def update(self, instance, validated_data):
        contacts_data = validated_data.pop('contacts')
        contacts_items_dict = dict((i.id, i) for i in instance.contacts.all())
        products_data = validated_data.pop('product')
        product_items_dict = dict((i.id, i) for i in instance.product.all())

        for contact in contacts_data:
            contacts_id = contact.get('id')
            if contacts_id:
                contacts_items_dict.pop(contacts_id)
                contacts = Contacts.objects.get(id=contacts_id)
                contacts.email = contact.get('email', contacts.email)
                contacts.country = contact.get('country', contacts.country)
                contacts.city = contact.get('city', contacts.city)
                contacts.street = contact.get('street', contacts.street)
                contacts.house = contact.get('house', contacts.house)
                contacts.save()
            else:
                Contacts.objects.create(company=instance, **contact)

        if len(contacts_items_dict) > 0:
            for item in contacts_items_dict:
                Contacts.objects.get(id=item).delete()

        for product_data in products_data:
            product_id = product_data.get('id')
            if product_id:
                product_items_dict.pop(product_id)
                product = Product.objects.get(id=product_id)
                product.title = product_data.get('title', product.title)
                product.model = product_data.get('model', product.model)
                product.save()
            else:
                Product.objects.create(company=instance, **product_data)

        if len(product_items_dict) > 0:
            for item in product_items_dict:
                Product.objects.get(id=item).delete()

        instance.title = validated_data.get('title', instance.title)
        instance.type = validated_data.get('type', instance.type)
        instance.supplier = validated_data.get('supplier', instance.supplier)
        instance.save()

        return instance
