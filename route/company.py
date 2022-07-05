from fastapi import APIRouter
from document.company import CompanyDocument
from model.request.request_company import CreateCompanyRequest
from model.response.response_company import CreateCompanyResponse
from repository.company import CompanyDatabase
from util.util_response import SuccessResponse

router_company = APIRouter()


@router_company.post("/company", response_model=CreateCompanyResponse)
async def add_company(
    req: CreateCompanyRequest,
    # current_user: JwtToken = Security(get_current_user, scopes=["superadmin"]),
):
    companySave = CompanyDocument(data=req)
    company = await CompanyDatabase.add_company(companySave)

    return SuccessResponse(company)


