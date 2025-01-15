from ..serializers import AccountSerializer


class AccountService:
    def __init__(self):
        pass

    def create_new_account(self, data):
        new_account = {
            **data,
            "is_active": True,
        }
        print(new_account, 1111)
        serialized_data = AccountSerializer(data=new_account)
        if serialized_data.is_valid():
            serialized_data.save()
            return {
                "success": True,
                "data": serialized_data.data,
            }
        else:
            print(f"Validation errors: {serialized_data.errors}")
            return {
                "success": False,
                "data": serialized_data.errors,
            }
