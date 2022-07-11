from typing import List, Union

from beanie import PydanticObjectId

from document.company import CompanyDocument

company_collection = CompanyDocument


class CompanyDatabase:
    async def get_companies() -> List[CompanyDocument]:
        companies = await company_collection.all().to_list()
        return companies

    async def add_company(new_company: CompanyDocument) -> CompanyDocument:
        company = await new_company.create()
        return company

    async def get_company(id: PydanticObjectId) -> CompanyDocument:
        company = await company_collection.get(id)
        if company:
            return company

    async def delete_company(id: PydanticObjectId) -> bool:
        company = await company_collection.get(id)
        if company:
            await company.delete()
            return True

    async def update_company_data(
        id: PydanticObjectId, data: dict
    ) -> Union[bool, CompanyDocument]:
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {field: value for field, value in des_body.items()}}
        company = await company_collection.get(id)
        if company:
            await company.update(update_query)
            return company
        return False
