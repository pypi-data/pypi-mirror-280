import requests
from bpiek import models

AUTH_URL = "https://bp.iek.ru/oauth/login"
API_URL = "https://bp.iek.ru/api/catalog/v1/"


class BPIekApi:
    def __init__(self, username, password) -> None:
        self.session = requests.Session()
        self.username = username
        self.password = password

        self._login()

    def _login(self) -> None:
        auth = self.session.post(
            url=f"{AUTH_URL}",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={"username": self.username, "password": self.password},
        )

    def _instance(self, endpoint, params: dict = {}):
        response = self.session.get(
            url=API_URL + endpoint,
            headers={"Content-Type": "application/json"},
            params={"format": "json", **params},
        )
        return response.json()

    def get_parent_categories(self) -> list[models.Category] | models.Error:
        response = self._instance("client/catalog")

        try:
            result: models.ParentCategoriesResponse = (
                models.ParentCategoriesResponse.model_validate(response)
            )

            return result.categories

        except Exception as e:
            return models.Error(code=400, message=str(e))

    def get_product_by_article(self, article: str) -> models.Product | models.Error:
        response = self._instance(f"client/products/{article}")

        try:
            result: models.Product = models.Product.model_validate(response)

            return result

        except Exception as e:
            return models.Error(code=400, message=str(e))

    def get_categories_and_products_by_slug_parent_category(
        self, slug
    ) -> models.CategoriesAndProductsBySlugParentCategory | models.Error:
        response = self._instance(f"client/category/{slug}/json")

        try:
            result: models.CategoriesAndProductsBySlugParentCategory = (
                models.CategoriesAndProductsBySlugParentCategory.model_validate(
                    response
                )
            )

            return result

        except Exception as e:
            return models.Error(code=400, message=str(e))

    def get_new_products(
        self,
        sortBy: str = "article",
        sortOrder: str = "asc",
        pageSize: int = 10,
        page: int = 1,
    ) -> models.NewProductsResponse | models.Error:
        response = self._instance(
            "new-products",
            {sortBy: sortBy, sortOrder: sortOrder, pageSize: pageSize, page: page},
        )

        try:
            result: models.NewProductsResponse = (
                models.NewProductsResponse.model_validate(response)
            )

            return result

        except Exception as e:
            return models.Error(code=400, message=str(e))

    def get_remains_and_planresidues(
        self, slug
    ) -> models.RemainsAndPlanresiduesResponse | models.Error:
        response = self._instance(f"client/category/{slug}/balances-json")

        try:
            result: models.RemainsAndPlanresiduesResponse = (
                models.RemainsAndPlanresiduesResponse.model_validate(response)
            )

            return result

        except Exception as e:
            return models.Error(code=400, message=str(e))
