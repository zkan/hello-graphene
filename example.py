import graphene


class Account(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


class Query(graphene.ObjectType):
    hello = graphene.String(description='A typical hello world')
    account = graphene.Field(Account)

    def resolve_hello(self, args, context, info):
        return 'World'

    def resolve_account(self, args, context, info):
        return Account(id=1, name='Pronto')


schema = graphene.Schema(query=Query)

query = '''
    query something {
        hello
        account {
            name
        }
    }
'''

result = schema.execute(query)

print(result.data)
print(result.data['hello'])
print(result.data['account'])
