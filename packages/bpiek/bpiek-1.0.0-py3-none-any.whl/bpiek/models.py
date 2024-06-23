from typing import Any
from pydantic import BaseModel, ConfigDict, Field
from pydantic.types import UUID1


class Category(BaseModel):
    slug: str  # Слаг категории
    name: str  # Название категории
    url: str  # Относительный адрес категории
    apiUrl: str  # Ссылка на скачивание файла с содержимым категории


class ProductShort(BaseModel):
    class WarehouseData(BaseModel):
        class Incoming(BaseModel):
            dateBegan: str | None
            dateEnd: str | None
            amount: int
            type: str  # Enum: "production" "shipping" Тип поступления, production - поступление после производства, shipping - доставка на склад

        warehouseId: UUID1
        warehouseName: str
        availableAmount: int
        incoming: list[Incoming]

    article: str  # Артикул товара
    name: str  # Полное наименование товара
    multiplicity: int | None  # Кратность продажи
    priceBase: float | None  # Базовая цена с НДС
    priceRrc: float | None  # Рекомендованная розничная цена (РРЦ) с НДС
    available: int | None  # Значение остатка
    units: str | None  # Единицы измерения
    warehouseData: list[WarehouseData]


class Product(ProductShort):
    class ImageVariant(BaseModel):
        url: str  # Ссылка
        ext: str  # Расширение
        width: int  # Ширина

    class Etim(BaseModel):
        class EtimClass(BaseModel):
            id: str
            name: str  # Название класса

        class EtimFeatures(BaseModel):
            id: str
            name: str  # Название свойства
            sort: int | None  # Порядок сортировки по умолчанию
            unit: str | None  # Единицы измерения
            value: str  # Значение свойства
            value_union: str  # Код значения

        etim_class: EtimClass = Field(alias="class")
        features: list[EtimFeatures]

    class Complects(BaseModel):
        article: str  # Артикул
        name: str  # Наименование
        quantity: int  # Количество

    class LeftPeriod(BaseModel):
        name: str  # Название характеристики
        value: str  # Значение характеристики

    class LeftPeriodRaw(BaseModel):
        class Lifespan(BaseModel):
            limit: str | None
            value: str | None
            units: str | None

        class Warranty(BaseModel):
            value: str | None
            units: str | None

        lifespan: Lifespan
        warranty: Warranty

    class LogisticParams(BaseModel):
        class Value(BaseModel):
            group: str | None
            individual: str | None
            transport: str | None

        name: str
        nameOrig: str
        value: Value

    class LogisticParamsData(BaseModel):
        class SinglePackage(BaseModel):
            multiplicity: int | None
            unit: str | None

        singlePackage: SinglePackage

    class DesignFeatures(BaseModel):
        imageUrl: str
        description: str

    class Videos(BaseModel):
        name: str
        description: str
        url: str
        type: str  # Enum: "url" "file"

    class Software(BaseModel):
        name: str
        description: str
        url: str
        size: str

    shortName: str  # Краткое название
    description: str | None  # Описание
    categoryName: str | None  # Название категории
    category: str  # Относительный путь до категории в каталоге
    slug: str  # Слаг товара
    tm: str  # Торговая марка
    url: str  # Ссылка на товар
    isArchived: bool  # Архивный или нет
    imageUrl: str  # Фото товара (основное)
    imageUrls: list[str]  # Все фото товара
    imageVariants: list[ImageVariant]  # Все вариации изображений
    advantages: str | None  # Преимущества
    etim: Etim  # EIM характеристики товара
    complects: list[Complects]  # Комплектация и сопутствующие товары
    complectations: str | None  # Комплектация
    files: list[Any]  # Список файлов, относящихся к товару (ГЧ, КД, CAD-модели и т.д.)
    leftPeriod: list[LeftPeriod] | None  # Характеристики срока службы
    leftPeriodRaw: LeftPeriodRaw  # Гарантийные показатели
    logisticParams: list[LogisticParams]  # Логистические характеристики
    logisticParamsData: (
        LogisticParamsData | None
    )  # Подробные логистические характеристики
    novelty: bool  # Новинка или нет
    designFeatures: list[DesignFeatures]  # Отличительные особенности
    videos: list[Videos]  # Видео по товару
    software: list[Software]  # ПО по товару
    banner: str | None  # Текст баннера
    lastModified: str | None  # Дата последнего изменения
    countryOfProduction: str | None  # Страна производства
    firstSaleDate: str | None  # Дата начала продаж
    feacn: str | None  # Код ТН ВЭД
    family: str | Any | None
    series: str | Any | None
    indPacking: list[str]  # Ссылки на фото упаковки
    analogs: list["Product"]  # Аналоги
    related: list["Product"]  # Совместно применяемые изделия
    qrCode: str | None = Field(default=None)
    isOutOfAssortment: bool
    isOutOfProduction: bool


class ParentCategoriesResponse(BaseModel):
    categories: list[Category]


class CategoriesAndProductsBySlugParentCategory(BaseModel):
    date: str
    slug: str
    name: str
    url: str
    categories: list[Category]
    products: list[Product]


class NewProductsResponse(BaseModel):
    class Data(BaseModel):
        products: list[Product]

    class Meta(BaseModel):
        page: str
        totalPages: int
        totalCount: int
        pageSize: int

    data: Data
    _meta: Meta


class RemainsAndPlanresiduesResponse(BaseModel):
    date: str
    products: list[ProductShort]


class Error(BaseModel):
    code: int
    message: str
