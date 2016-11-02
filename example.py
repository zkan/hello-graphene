import graphene


class GeoInput(graphene.InputObjectType):
    lat = graphene.Float(required=True)
    lng = graphene.Float(required=True)


class Address(graphene.ObjectType):
    latlng = graphene.String()


class Account(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


class Query(graphene.ObjectType):
    hello = graphene.String(description='A typical hello world')
    account = graphene.Field(Account)
    address = graphene.Field(Address, geo=GeoInput())

    def resolve_hello(self, args, context, info):
        return 'World'

    def resolve_account(self, args, context, info):
        return Account(id=1, name='Pronto')

    def resolve_address(self, args, context, info):
        geo = args.get('geo')
        return Address(latlng="({},{})".format(geo.get('lat'), geo.get('lng')))


schema = graphene.Schema(query=Query)

query = '''
    query something {
        hello
        account {
            name
        }
        address(geo: {lat: 32.2, lng: 12}) {
            latlng
        }
    }
'''

result = schema.execute(query)

print(result.data)
print(result.data['hello'])
print(result.data['account']['name'])
print(result.data['address']['latlng'])
