# Generated by ariadne-codegen
# Source: ../api-client-schema/src/generated/schema.graphql

from enum import Enum


class AccessDeniedReason(str, Enum):
    BudgetExceeded = "BudgetExceeded"
    CustomerIsArchived = "CustomerIsArchived"
    CustomerNotFound = "CustomerNotFound"
    CustomerResourceNotFound = "CustomerResourceNotFound"
    FeatureNotFound = "FeatureNotFound"
    NoActiveSubscription = "NoActiveSubscription"
    NoFeatureEntitlementInSubscription = "NoFeatureEntitlementInSubscription"
    RequestedUsageExceedingLimit = "RequestedUsageExceedingLimit"
    Unknown = "Unknown"


class AccountStatus(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"


class AddonSortFields(str, Enum):
    billingId = "billingId"
    createdAt = "createdAt"
    description = "description"
    displayName = "displayName"
    environmentId = "environmentId"
    id = "id"
    isLatest = "isLatest"
    pricingType = "pricingType"
    productId = "productId"
    refId = "refId"
    status = "status"
    updatedAt = "updatedAt"
    versionNumber = "versionNumber"


class AggregationFunction(str, Enum):
    AVG = "AVG"
    COUNT = "COUNT"
    MAX = "MAX"
    MIN = "MIN"
    SUM = "SUM"
    UNIQUE = "UNIQUE"


class Alignment(str, Enum):
    CENTER = "CENTER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class ApiKeySortFields(str, Enum):
    id = "id"


class ApiKeyType(str, Enum):
    CLIENT = "CLIENT"
    SALESFORCE = "SALESFORCE"
    SERVER = "SERVER"


class BillingAnchor(str, Enum):
    START_OF_THE_MONTH = "START_OF_THE_MONTH"
    SUBSCRIPTION_START = "SUBSCRIPTION_START"


class BillingCadence(str, Enum):
    ONE_OFF = "ONE_OFF"
    RECURRING = "RECURRING"


class BillingModel(str, Enum):
    FLAT_FEE = "FLAT_FEE"
    PER_UNIT = "PER_UNIT"
    USAGE_BASED = "USAGE_BASED"


class BillingPeriod(str, Enum):
    ANNUALLY = "ANNUALLY"
    MONTHLY = "MONTHLY"


class BillingVendorIdentifier(str, Enum):
    STRIPE = "STRIPE"


class ChangeType(str, Enum):
    ADDED = "ADDED"
    DELETED = "DELETED"
    MODIFIED = "MODIFIED"
    REORDERED = "REORDERED"


class ConditionOperation(str, Enum):
    EQUALS = "EQUALS"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
    IS_NOT_NULL = "IS_NOT_NULL"
    IS_NULL = "IS_NULL"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"
    NOT_EQUALS = "NOT_EQUALS"


class CouponSortFields(str, Enum):
    billingId = "billingId"
    createdAt = "createdAt"
    description = "description"
    environmentId = "environmentId"
    id = "id"
    name = "name"
    refId = "refId"
    status = "status"
    type = "type"
    updatedAt = "updatedAt"


class CouponStatus(str, Enum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"


class CouponType(str, Enum):
    FIXED = "FIXED"
    PERCENTAGE = "PERCENTAGE"


class Currency(str, Enum):
    AED = "AED"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BSD = "BSD"
    BWP = "BWP"
    BYN = "BYN"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHF = "CHF"
    CLP = "CLP"
    CNY = "CNY"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    GBP = "GBP"
    GEL = "GEL"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GYD = "GYD"
    HKD = "HKD"
    HRK = "HRK"
    HTG = "HTG"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    ISK = "ISK"
    JMD = "JMD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KRW = "KRW"
    KYD = "KYD"
    KZT = "KZT"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRO = "MRO"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SEK = "SEK"
    SGD = "SGD"
    SLE = "SLE"
    SLL = "SLL"
    SOS = "SOS"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    UZS = "UZS"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XCD = "XCD"
    XOF = "XOF"
    XPF = "XPF"
    YER = "YER"
    ZAR = "ZAR"
    ZMW = "ZMW"


class CustomerResourceSortFields(str, Enum):
    createdAt = "createdAt"
    environmentId = "environmentId"
    resourceId = "resourceId"


class CustomerSortFields(str, Enum):
    billingId = "billingId"
    createdAt = "createdAt"
    crmHubspotCompanyId = "crmHubspotCompanyId"
    crmHubspotCompanyUrl = "crmHubspotCompanyUrl"
    crmId = "crmId"
    customerId = "customerId"
    deletedAt = "deletedAt"
    email = "email"
    environmentId = "environmentId"
    id = "id"
    name = "name"
    refId = "refId"
    searchQuery = "searchQuery"
    updatedAt = "updatedAt"


class CustomerSubscriptionSortFields(str, Enum):
    billingId = "billingId"
    cancelReason = "cancelReason"
    cancellationDate = "cancellationDate"
    createdAt = "createdAt"
    crmId = "crmId"
    crmLinkUrl = "crmLinkUrl"
    currentBillingPeriodEnd = "currentBillingPeriodEnd"
    currentBillingPeriodStart = "currentBillingPeriodStart"
    customerId = "customerId"
    effectiveEndDate = "effectiveEndDate"
    endDate = "endDate"
    environmentId = "environmentId"
    id = "id"
    oldBillingId = "oldBillingId"
    paymentCollection = "paymentCollection"
    pricingType = "pricingType"
    refId = "refId"
    resourceId = "resourceId"
    startDate = "startDate"
    status = "status"
    subscriptionId = "subscriptionId"
    trialEndDate = "trialEndDate"


class Department(str, Enum):
    CEO_OR_FOUNDER = "CEO_OR_FOUNDER"
    ENGINEERING = "ENGINEERING"
    GROWTH = "GROWTH"
    MARKETING = "MARKETING"
    MONETIZATION = "MONETIZATION"
    OTHER = "OTHER"
    PRODUCT = "PRODUCT"


class DiscountDurationType(str, Enum):
    FOREVER = "FOREVER"
    ONCE = "ONCE"
    REPEATING = "REPEATING"


class DiscountType(str, Enum):
    FIXED = "FIXED"
    PERCENTAGE = "PERCENTAGE"


class EntitlementBehavior(str, Enum):
    Increment = "Increment"
    Override = "Override"


class EntitlementResetPeriod(str, Enum):
    DAY = "DAY"
    HOUR = "HOUR"
    MONTH = "MONTH"
    WEEK = "WEEK"
    YEAR = "YEAR"


class EntitySelectionMode(str, Enum):
    BLACK_LIST = "BLACK_LIST"
    WHITE_LIST = "WHITE_LIST"


class EnvironmentProvisionStatus(str, Enum):
    DONE = "DONE"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    NOT_PROVISIONED = "NOT_PROVISIONED"


class EnvironmentSortFields(str, Enum):
    createdAt = "createdAt"
    displayName = "displayName"
    id = "id"
    permanentDeletionDate = "permanentDeletionDate"
    slug = "slug"


class EnvironmentType(str, Enum):
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"
    SANDBOX = "SANDBOX"


class ErrorCode(str, Enum):
    AccountNotFoundError = "AccountNotFoundError"
    AddonDependencyMissingError = "AddonDependencyMissingError"
    AddonHasToHavePriceError = "AddonHasToHavePriceError"
    AddonNotFound = "AddonNotFound"
    AddonQuantityExceedsLimitError = "AddonQuantityExceedsLimitError"
    AddonWithDraftCannotBeDeletedError = "AddonWithDraftCannotBeDeletedError"
    AmountTooLarge = "AmountTooLarge"
    ArchivedCouponCantBeApplied = "ArchivedCouponCantBeApplied"
    AuthCustomerMismatch = "AuthCustomerMismatch"
    AuthCustomerReadonly = "AuthCustomerReadonly"
    AwsMarketplaceIntegrationError = "AwsMarketplaceIntegrationError"
    AwsMarketplaceIntegrationValidationError = (
        "AwsMarketplaceIntegrationValidationError"
    )
    BadUserInput = "BadUserInput"
    BillingIntegrationAlreadyExistsError = "BillingIntegrationAlreadyExistsError"
    BillingIntegrationMissing = "BillingIntegrationMissing"
    BillingPeriodMissingError = "BillingPeriodMissingError"
    CannotAddOverrideEntitlementToPlan = "CannotAddOverrideEntitlementToPlan"
    CannotArchiveFeatureError = "CannotArchiveFeatureError"
    CannotDeleteCustomerError = "CannotDeleteCustomerError"
    CannotDeleteFeatureError = "CannotDeleteFeatureError"
    CannotDeleteProductError = "CannotDeleteProductError"
    CannotEditPackageInNonDraftMode = "CannotEditPackageInNonDraftMode"
    CannotRemovePaymentMethodFromCustomerError = (
        "CannotRemovePaymentMethodFromCustomerError"
    )
    CannotReportUsageForEntitlementWithMeterError = (
        "CannotReportUsageForEntitlementWithMeterError"
    )
    CannotUpdateUnitTransformationError = "CannotUpdateUnitTransformationError"
    CannotUpsertToPackageThatHasDraft = "CannotUpsertToPackageThatHasDraft"
    CheckoutIsNotSupported = "CheckoutIsNotSupported"
    CouponNotFound = "CouponNotFound"
    CustomerAlreadyHaveCustomerCoupon = "CustomerAlreadyHaveCustomerCoupon"
    CustomerAlreadyUsesCoupon = "CustomerAlreadyUsesCoupon"
    CustomerHasNoEmailAddress = "CustomerHasNoEmailAddress"
    CustomerNoBillingId = "CustomerNoBillingId"
    CustomerNotFound = "CustomerNotFound"
    CustomerResourceNotFound = "CustomerResourceNotFound"
    DowngradeBillingPeriodNotSupportedError = "DowngradeBillingPeriodNotSupportedError"
    DraftPlanCantBeArchived = "DraftPlanCantBeArchived"
    DuplicateAddonProvisionedError = "DuplicateAddonProvisionedError"
    DuplicateProductValidationError = "DuplicateProductValidationError"
    DuplicatedEntityNotAllowed = "DuplicatedEntityNotAllowed"
    EditAllowedOnDraftPackageOnlyError = "EditAllowedOnDraftPackageOnlyError"
    EntitlementLimitExceededError = "EntitlementLimitExceededError"
    EntitlementUsageOutOfRangeError = "EntitlementUsageOutOfRangeError"
    EntitlementsMustBelongToSamePackage = "EntitlementsMustBelongToSamePackage"
    EntityIdDifferentFromRefIdError = "EntityIdDifferentFromRefIdError"
    EntityIsArchivedError = "EntityIsArchivedError"
    EnvironmentMissing = "EnvironmentMissing"
    ExperimentAlreadyRunning = "ExperimentAlreadyRunning"
    ExperimentNotFoundError = "ExperimentNotFoundError"
    ExperimentStatusError = "ExperimentStatusError"
    FailedToCreateCheckoutSessionError = "FailedToCreateCheckoutSessionError"
    FailedToImportCustomer = "FailedToImportCustomer"
    FeatureNotFound = "FeatureNotFound"
    FetchAllCountriesPricesNotAllowed = "FetchAllCountriesPricesNotAllowed"
    FreePlanCantHaveCompatiblePackageGroupError = (
        "FreePlanCantHaveCompatiblePackageGroupError"
    )
    HubspotIntegrationError = "HubspotIntegrationError"
    IdentityForbidden = "IdentityForbidden"
    ImportAlreadyInProgress = "ImportAlreadyInProgress"
    ImportSubscriptionsBulkError = "ImportSubscriptionsBulkError"
    InitStripePaymentMethodError = "InitStripePaymentMethodError"
    IntegrationNotFound = "IntegrationNotFound"
    IntegrationValidationError = "IntegrationValidationError"
    IntegrityViolation = "IntegrityViolation"
    InvalidAddressError = "InvalidAddressError"
    InvalidArgumentError = "InvalidArgumentError"
    InvalidCancellationDate = "InvalidCancellationDate"
    InvalidEntitlementResetPeriod = "InvalidEntitlementResetPeriod"
    InvalidMemberDelete = "InvalidMemberDelete"
    InvalidMetadataError = "InvalidMetadataError"
    InvalidQuantity = "InvalidQuantity"
    InvalidSubscriptionStatus = "InvalidSubscriptionStatus"
    InvalidUpdatePriceUnitAmountError = "InvalidUpdatePriceUnitAmountError"
    MemberInvitationError = "MemberInvitationError"
    MemberNotFound = "MemberNotFound"
    MergeEnvironmentValidationError = "MergeEnvironmentValidationError"
    MeterMustBeAssociatedToMeteredFeature = "MeterMustBeAssociatedToMeteredFeature"
    MeteringNotAvailableForFeatureType = "MeteringNotAvailableForFeatureType"
    MissingEntityIdError = "MissingEntityIdError"
    MissingSubscriptionInvoiceError = "MissingSubscriptionInvoiceError"
    MultiSubscriptionCantBeAutoCancellationSourceError = (
        "MultiSubscriptionCantBeAutoCancellationSourceError"
    )
    NoFeatureEntitlementError = "NoFeatureEntitlementError"
    NoFeatureEntitlementInSubscription = "NoFeatureEntitlementInSubscription"
    NoProductsAvailable = "NoProductsAvailable"
    OperationNotAllowedDuringInProgressExperiment = (
        "OperationNotAllowedDuringInProgressExperiment"
    )
    PackageAlreadyPublished = "PackageAlreadyPublished"
    PackageGroupMinItemsError = "PackageGroupMinItemsError"
    PackageGroupNotFound = "PackageGroupNotFound"
    PackagePricingTypeNotSet = "PackagePricingTypeNotSet"
    PaymentMethodNotFoundError = "PaymentMethodNotFoundError"
    PlanCannotBePublishWhenBasePlanIsDraft = "PlanCannotBePublishWhenBasePlanIsDraft"
    PlanCannotBePublishWhenCompatibleAddonIsDraft = (
        "PlanCannotBePublishWhenCompatibleAddonIsDraft"
    )
    PlanIsUsedAsDefaultStartPlan = "PlanIsUsedAsDefaultStartPlan"
    PlanIsUsedAsDowngradePlan = "PlanIsUsedAsDowngradePlan"
    PlanNotFound = "PlanNotFound"
    PlanWithChildCantBeDeleted = "PlanWithChildCantBeDeleted"
    PlansCircularDependencyError = "PlansCircularDependencyError"
    PreparePaymentMethodFormError = "PreparePaymentMethodFormError"
    PriceNotFound = "PriceNotFound"
    ProductNotFoundError = "ProductNotFoundError"
    PromotionCodeCustomerNotFirstPurchase = "PromotionCodeCustomerNotFirstPurchase"
    PromotionCodeMaxRedemptionsReached = "PromotionCodeMaxRedemptionsReached"
    PromotionCodeMinimumAmountNotReached = "PromotionCodeMinimumAmountNotReached"
    PromotionCodeNotActive = "PromotionCodeNotActive"
    PromotionCodeNotForCustomer = "PromotionCodeNotForCustomer"
    PromotionCodeNotFound = "PromotionCodeNotFound"
    PromotionalEntitlementNotFoundError = "PromotionalEntitlementNotFoundError"
    RateLimitExceeded = "RateLimitExceeded"
    RecalculateEntitlementsError = "RecalculateEntitlementsError"
    ResyncAlreadyInProgress = "ResyncAlreadyInProgress"
    ScheduledMigrationAlreadyExistsError = "ScheduledMigrationAlreadyExistsError"
    SelectedBillingModelDoesntMatchImportedItemError = (
        "SelectedBillingModelDoesntMatchImportedItemError"
    )
    SingleSubscriptionCantBeAutoCancellationTargetError = (
        "SingleSubscriptionCantBeAutoCancellationTargetError"
    )
    StripeCustomerIsDeleted = "StripeCustomerIsDeleted"
    StripeError = "StripeError"
    SubscriptionAlreadyCanceledOrExpired = "SubscriptionAlreadyCanceledOrExpired"
    SubscriptionAlreadyOnLatestPlanError = "SubscriptionAlreadyOnLatestPlanError"
    SubscriptionDoesNotHaveBillingPeriod = "SubscriptionDoesNotHaveBillingPeriod"
    SubscriptionInvoiceStatusError = "SubscriptionInvoiceStatusError"
    SubscriptionMustHaveSinglePlanError = "SubscriptionMustHaveSinglePlanError"
    SubscriptionNoBillingId = "SubscriptionNoBillingId"
    SubscriptionNotFound = "SubscriptionNotFound"
    TooManySubscriptionsPerCustomer = "TooManySubscriptionsPerCustomer"
    TrialMinDateError = "TrialMinDateError"
    TrialMustBeCancelledImmediately = "TrialMustBeCancelledImmediately"
    UnPublishedPackage = "UnPublishedPackage"
    Unauthenticated = "Unauthenticated"
    UncompatibleSubscriptionAddon = "UncompatibleSubscriptionAddon"
    UnexpectedError = "UnexpectedError"
    UnsupportedFeatureType = "UnsupportedFeatureType"
    UnsupportedSubscriptionScheduleType = "UnsupportedSubscriptionScheduleType"
    UnsupportedVendorIdentifier = "UnsupportedVendorIdentifier"
    UsageMeasurementDiffOutOfRangeError = "UsageMeasurementDiffOutOfRangeError"


class EventActor(str, Enum):
    APP_CUSTOMER = "APP_CUSTOMER"
    APP_PUBLIC = "APP_PUBLIC"
    APP_SERVER = "APP_SERVER"
    AWS = "AWS"
    IMPORT = "IMPORT"
    MIGRATION = "MIGRATION"
    SALESFORCE = "SALESFORCE"
    SCHEDULER = "SCHEDULER"
    SERVICE = "SERVICE"
    STRIPE = "STRIPE"
    SUPPORT = "SUPPORT"
    SYSTEM = "SYSTEM"
    USER = "USER"


class EventEntityType(str, Enum):
    ADDON = "ADDON"
    COUPON = "COUPON"
    CUSTOMER = "CUSTOMER"
    ENTITLEMENT = "ENTITLEMENT"
    FEATURE = "FEATURE"
    IMPORT = "IMPORT"
    MEASUREMENT = "MEASUREMENT"
    PACKAGE = "PACKAGE"
    PACKAGE_GROUP = "PACKAGE_GROUP"
    PLAN = "PLAN"
    PRODUCT = "PRODUCT"
    PROMOTIONAL_ENTITLEMENT = "PROMOTIONAL_ENTITLEMENT"
    SUBSCRIPTION = "SUBSCRIPTION"


class EventLogSortFields(str, Enum):
    createdAt = "createdAt"
    entityId = "entityId"
    environmentId = "environmentId"
    eventLogType = "eventLogType"
    id = "id"
    parentEntityId = "parentEntityId"


class EventLogType(str, Enum):
    ADDON_CREATED = "ADDON_CREATED"
    ADDON_DELETED = "ADDON_DELETED"
    ADDON_UPDATED = "ADDON_UPDATED"
    COUPON_ARCHIVED = "COUPON_ARCHIVED"
    COUPON_CREATED = "COUPON_CREATED"
    COUPON_UPDATED = "COUPON_UPDATED"
    CREATE_SUBSCRIPTION_FAILED = "CREATE_SUBSCRIPTION_FAILED"
    CUSTOMER_CREATED = "CUSTOMER_CREATED"
    CUSTOMER_DELETED = "CUSTOMER_DELETED"
    CUSTOMER_ENTITLEMENT_CALCULATION_TRIGGERED = (
        "CUSTOMER_ENTITLEMENT_CALCULATION_TRIGGERED"
    )
    CUSTOMER_PAYMENT_FAILED = "CUSTOMER_PAYMENT_FAILED"
    CUSTOMER_RESOURCE_ENTITLEMENT_CALCULATION_TRIGGERED = (
        "CUSTOMER_RESOURCE_ENTITLEMENT_CALCULATION_TRIGGERED"
    )
    CUSTOMER_UPDATED = "CUSTOMER_UPDATED"
    EDGE_API_CUSTOMER_DATA_RESYNC = "EDGE_API_CUSTOMER_DATA_RESYNC"
    EDGE_API_DATA_RESYNC = "EDGE_API_DATA_RESYNC"
    EDGE_API_DOGGO_RESYNC = "EDGE_API_DOGGO_RESYNC"
    EDGE_API_PACKAGE_ENTITLEMENTS_DATA_RESYNC = (
        "EDGE_API_PACKAGE_ENTITLEMENTS_DATA_RESYNC"
    )
    EDGE_API_SUBSCRIPTIONS_DATA_RESYNC = "EDGE_API_SUBSCRIPTIONS_DATA_RESYNC"
    ENTITLEMENTS_UPDATED = "ENTITLEMENTS_UPDATED"
    ENTITLEMENT_DENIED = "ENTITLEMENT_DENIED"
    ENTITLEMENT_GRANTED = "ENTITLEMENT_GRANTED"
    ENTITLEMENT_REQUESTED = "ENTITLEMENT_REQUESTED"
    ENTITLEMENT_USAGE_EXCEEDED = "ENTITLEMENT_USAGE_EXCEEDED"
    ENVIRONMENT_DELETED = "ENVIRONMENT_DELETED"
    FEATURE_ARCHIVED = "FEATURE_ARCHIVED"
    FEATURE_CREATED = "FEATURE_CREATED"
    FEATURE_DELETED = "FEATURE_DELETED"
    FEATURE_UPDATED = "FEATURE_UPDATED"
    IMPORT_INTEGRATION_CATALOG_TRIGGERED = "IMPORT_INTEGRATION_CATALOG_TRIGGERED"
    IMPORT_INTEGRATION_CUSTOMERS_TRIGGERED = "IMPORT_INTEGRATION_CUSTOMERS_TRIGGERED"
    IMPORT_SUBSCRIPTIONS_BULK_TRIGGERED = "IMPORT_SUBSCRIPTIONS_BULK_TRIGGERED"
    MEASUREMENT_REPORTED = "MEASUREMENT_REPORTED"
    PACKAGE_GROUP_CREATED = "PACKAGE_GROUP_CREATED"
    PACKAGE_GROUP_UPDATED = "PACKAGE_GROUP_UPDATED"
    PACKAGE_PUBLISHED = "PACKAGE_PUBLISHED"
    PLAN_CREATED = "PLAN_CREATED"
    PLAN_DELETED = "PLAN_DELETED"
    PLAN_UPDATED = "PLAN_UPDATED"
    PRODUCT_CREATED = "PRODUCT_CREATED"
    PRODUCT_DELETED = "PRODUCT_DELETED"
    PRODUCT_UPDATED = "PRODUCT_UPDATED"
    PROMOTIONAL_ENTITLEMENT_EXPIRED = "PROMOTIONAL_ENTITLEMENT_EXPIRED"
    PROMOTIONAL_ENTITLEMENT_GRANTED = "PROMOTIONAL_ENTITLEMENT_GRANTED"
    PROMOTIONAL_ENTITLEMENT_REVOKED = "PROMOTIONAL_ENTITLEMENT_REVOKED"
    PROMOTIONAL_ENTITLEMENT_UPDATED = "PROMOTIONAL_ENTITLEMENT_UPDATED"
    RECALCULATE_ENTITLEMENTS_TRIGGERED = "RECALCULATE_ENTITLEMENTS_TRIGGERED"
    RESYNC_INTEGRATION_TRIGGERED = "RESYNC_INTEGRATION_TRIGGERED"
    SUBSCRIPTIONS_MIGRATED = "SUBSCRIPTIONS_MIGRATED"
    SUBSCRIPTIONS_MIGRATION_TRIGGERED = "SUBSCRIPTIONS_MIGRATION_TRIGGERED"
    SUBSCRIPTION_BILLING_MONTH_ENDS_SOON = "SUBSCRIPTION_BILLING_MONTH_ENDS_SOON"
    SUBSCRIPTION_CANCELED = "SUBSCRIPTION_CANCELED"
    SUBSCRIPTION_CREATED = "SUBSCRIPTION_CREATED"
    SUBSCRIPTION_EXPIRED = "SUBSCRIPTION_EXPIRED"
    SUBSCRIPTION_SPENT_LIMIT_EXCEEDED = "SUBSCRIPTION_SPENT_LIMIT_EXCEEDED"
    SUBSCRIPTION_TRIAL_CONVERTED = "SUBSCRIPTION_TRIAL_CONVERTED"
    SUBSCRIPTION_TRIAL_ENDS_SOON = "SUBSCRIPTION_TRIAL_ENDS_SOON"
    SUBSCRIPTION_TRIAL_EXPIRED = "SUBSCRIPTION_TRIAL_EXPIRED"
    SUBSCRIPTION_TRIAL_STARTED = "SUBSCRIPTION_TRIAL_STARTED"
    SUBSCRIPTION_UPDATED = "SUBSCRIPTION_UPDATED"
    SUBSCRIPTION_USAGE_CHARGE_TRIGGERED = "SUBSCRIPTION_USAGE_CHARGE_TRIGGERED"
    SUBSCRIPTION_USAGE_UPDATED = "SUBSCRIPTION_USAGE_UPDATED"
    SYNC_FAILED = "SYNC_FAILED"
    WIDGET_CONFIGURATION_UPDATED = "WIDGET_CONFIGURATION_UPDATED"


class ExperimentSortFields(str, Enum):
    createdAt = "createdAt"
    environmentId = "environmentId"
    id = "id"
    name = "name"
    productId = "productId"
    refId = "refId"
    status = "status"


class ExperimentStatus(str, Enum):
    COMPLETED = "COMPLETED"
    DRAFT = "DRAFT"
    IN_PROGRESS = "IN_PROGRESS"


class FeatureSortFields(str, Enum):
    createdAt = "createdAt"
    description = "description"
    displayName = "displayName"
    environmentId = "environmentId"
    featureStatus = "featureStatus"
    featureType = "featureType"
    id = "id"
    meterType = "meterType"
    refId = "refId"
    updatedAt = "updatedAt"


class FeatureStatus(str, Enum):
    ACTIVE = "ACTIVE"
    NEW = "NEW"
    SUSPENDED = "SUSPENDED"


class FeatureType(str, Enum):
    BOOLEAN = "BOOLEAN"
    NUMBER = "NUMBER"


class FontWeight(str, Enum):
    BOLD = "BOLD"
    NORMAL = "NORMAL"


class HookSortFields(str, Enum):
    createdAt = "createdAt"
    endpoint = "endpoint"
    environmentId = "environmentId"
    id = "id"
    status = "status"


class HookStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class ImportIntegrationTaskSortFields(str, Enum):
    createdAt = "createdAt"
    environmentId = "environmentId"
    id = "id"
    status = "status"
    taskType = "taskType"


class IntegrationSortFields(str, Enum):
    createdAt = "createdAt"
    environmentId = "environmentId"
    id = "id"
    vendorIdentifier = "vendorIdentifier"


class InvoiceLineItemType(str, Enum):
    AddonCharge = "AddonCharge"
    BaseCharge = "BaseCharge"
    InAdvanceCommitmentCharge = "InAdvanceCommitmentCharge"
    MinimumSpendAdjustmentCharge = "MinimumSpendAdjustmentCharge"
    Other = "Other"
    OverageCharge = "OverageCharge"
    PayAsYouGoCharge = "PayAsYouGoCharge"
    TierCharge = "TierCharge"


class MemberSortFields(str, Enum):
    createdAt = "createdAt"
    id = "id"


class MemberStatus(str, Enum):
    INVITED = "INVITED"
    REGISTERED = "REGISTERED"


class MeterType(str, Enum):
    FLUCTUATING = "Fluctuating"
    INCREMENTAL = "Incremental"
    None_ = "None"


class MonthlyAccordingTo(str, Enum):
    StartOfTheMonth = "StartOfTheMonth"
    SubscriptionStart = "SubscriptionStart"


class OverageBillingPeriod(str, Enum):
    MONTHLY = "MONTHLY"
    ON_SUBSCRIPTION_RENEWAL = "ON_SUBSCRIPTION_RENEWAL"


class PackageDTOSortFields(str, Enum):
    billingId = "billingId"
    createdAt = "createdAt"
    description = "description"
    displayName = "displayName"
    environmentId = "environmentId"
    id = "id"
    isLatest = "isLatest"
    pricingType = "pricingType"
    productId = "productId"
    refId = "refId"
    status = "status"
    updatedAt = "updatedAt"
    versionNumber = "versionNumber"


class PackageEntitlementSortFields(str, Enum):
    createdAt = "createdAt"
    environmentId = "environmentId"
    id = "id"
    packageId = "packageId"
    updatedAt = "updatedAt"


class PackageGroupSortFields(str, Enum):
    createdAt = "createdAt"
    displayName = "displayName"
    environmentId = "environmentId"
    isLatest = "isLatest"
    packageGroupId = "packageGroupId"
    productId = "productId"
    status = "status"
    updatedAt = "updatedAt"
    versionNumber = "versionNumber"


class PackageGroupStatus(str, Enum):
    ARCHIVED = "ARCHIVED"
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"


class PackageStatus(str, Enum):
    ARCHIVED = "ARCHIVED"
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"


class PaymentCollection(str, Enum):
    ACTION_REQUIRED = "ACTION_REQUIRED"
    FAILED = "FAILED"
    NOT_REQUIRED = "NOT_REQUIRED"
    PROCESSING = "PROCESSING"


class PaymentCollectionMethod(str, Enum):
    CHARGE = "CHARGE"
    INVOICE = "INVOICE"
    NONE = "NONE"


class PaymentMethodType(str, Enum):
    BANK = "BANK"
    CARD = "CARD"


class PlanChangeType(str, Enum):
    DOWNGRADE = "DOWNGRADE"
    NONE = "NONE"
    UPGRADE = "UPGRADE"


class PlanSortFields(str, Enum):
    billingId = "billingId"
    createdAt = "createdAt"
    description = "description"
    displayName = "displayName"
    environmentId = "environmentId"
    id = "id"
    isLatest = "isLatest"
    pricingType = "pricingType"
    productId = "productId"
    refId = "refId"
    status = "status"
    updatedAt = "updatedAt"
    versionNumber = "versionNumber"


class PriceSortFields(str, Enum):
    billingCadence = "billingCadence"
    billingId = "billingId"
    billingModel = "billingModel"
    billingPeriod = "billingPeriod"
    createdAt = "createdAt"
    id = "id"
    tiersMode = "tiersMode"


class PricingType(str, Enum):
    CUSTOM = "CUSTOM"
    FREE = "FREE"
    PAID = "PAID"


class ProductSortFields(str, Enum):
    awsMarketplaceProductCode = "awsMarketplaceProductCode"
    awsMarketplaceProductId = "awsMarketplaceProductId"
    createdAt = "createdAt"
    description = "description"
    displayName = "displayName"
    environmentId = "environmentId"
    id = "id"
    isDefaultProduct = "isDefaultProduct"
    multipleSubscriptions = "multipleSubscriptions"
    refId = "refId"
    updatedAt = "updatedAt"


class PromotionalEntitlementPeriod(str, Enum):
    CUSTOM = "CUSTOM"
    LIFETIME = "LIFETIME"
    ONE_MONTH = "ONE_MONTH"
    ONE_WEEK = "ONE_WEEK"
    ONE_YEAR = "ONE_YEAR"
    SIX_MONTH = "SIX_MONTH"


class PromotionalEntitlementSortFields(str, Enum):
    createdAt = "createdAt"
    environmentId = "environmentId"
    id = "id"
    status = "status"
    updatedAt = "updatedAt"


class PromotionalEntitlementStatus(str, Enum):
    Active = "Active"
    Expired = "Expired"
    Paused = "Paused"


class ProrationBehavior(str, Enum):
    CREATE_PRORATIONS = "CREATE_PRORATIONS"
    INVOICE_IMMEDIATELY = "INVOICE_IMMEDIATELY"


class ProvisionSubscriptionStatus(str, Enum):
    PAYMENT_REQUIRED = "PAYMENT_REQUIRED"
    SUCCESS = "SUCCESS"


class PublishMigrationType(str, Enum):
    ALL_CUSTOMERS = "ALL_CUSTOMERS"
    NEW_CUSTOMERS = "NEW_CUSTOMERS"


class ScheduleStrategy(str, Enum):
    END_OF_BILLING_MONTH = "END_OF_BILLING_MONTH"
    END_OF_BILLING_PERIOD = "END_OF_BILLING_PERIOD"
    IMMEDIATE = "IMMEDIATE"


class SortDirection(str, Enum):
    ASC = "ASC"
    DESC = "DESC"


class SortNulls(str, Enum):
    NULLS_FIRST = "NULLS_FIRST"
    NULLS_LAST = "NULLS_LAST"


class SourceType(str, Enum):
    JS_CLIENT_SDK = "JS_CLIENT_SDK"
    NODE_SERVER_SDK = "NODE_SERVER_SDK"
    PERSISTENT_CACHE_SERVICE = "PERSISTENT_CACHE_SERVICE"


class SubscriptionAddonSortFields(str, Enum):
    createdAt = "createdAt"
    id = "id"
    quantity = "quantity"
    updatedAt = "updatedAt"


class SubscriptionCancelReason(str, Enum):
    AutoCancellationRule = "AutoCancellationRule"
    CancelledByBilling = "CancelledByBilling"
    CustomerArchived = "CustomerArchived"
    DetachBilling = "DetachBilling"
    Expired = "Expired"
    Immediate = "Immediate"
    PendingPaymentExpired = "PendingPaymentExpired"
    ScheduledCancellation = "ScheduledCancellation"
    TrialConverted = "TrialConverted"
    TrialEnded = "TrialEnded"
    UpgradeOrDowngrade = "UpgradeOrDowngrade"


class SubscriptionCancellationAction(str, Enum):
    DEFAULT = "DEFAULT"
    REVOKE_ENTITLEMENTS = "REVOKE_ENTITLEMENTS"


class SubscriptionCancellationTime(str, Enum):
    END_OF_BILLING_PERIOD = "END_OF_BILLING_PERIOD"
    IMMEDIATE = "IMMEDIATE"
    SPECIFIC_DATE = "SPECIFIC_DATE"


class SubscriptionDecisionStrategy(str, Enum):
    PREDEFINED_FREE_PLAN = "PREDEFINED_FREE_PLAN"
    PREDEFINED_TRIAL_PLAN = "PREDEFINED_TRIAL_PLAN"
    REQUESTED_PLAN = "REQUESTED_PLAN"
    SKIPPED_SUBSCRIPTION_CREATION = "SKIPPED_SUBSCRIPTION_CREATION"


class SubscriptionEndSetup(str, Enum):
    CANCEL_SUBSCRIPTION = "CANCEL_SUBSCRIPTION"
    DOWNGRADE_TO_FREE = "DOWNGRADE_TO_FREE"


class SubscriptionEntitlementSortFields(str, Enum):
    createdAt = "createdAt"
    environmentId = "environmentId"
    id = "id"
    subscriptionId = "subscriptionId"
    updatedAt = "updatedAt"


class SubscriptionInvoiceBillingReason(str, Enum):
    BILLING_CYCLE = "BILLING_CYCLE"
    MANUAL = "MANUAL"
    MINIMUM_INVOICE_AMOUNT_EXCEEDED = "MINIMUM_INVOICE_AMOUNT_EXCEEDED"
    OTHER = "OTHER"
    SUBSCRIPTION_CREATION = "SUBSCRIPTION_CREATION"
    SUBSCRIPTION_UPDATE = "SUBSCRIPTION_UPDATE"


class SubscriptionInvoiceStatus(str, Enum):
    CANCELED = "CANCELED"
    OPEN = "OPEN"
    PAID = "PAID"


class SubscriptionMigrationTaskSortFields(str, Enum):
    createdAt = "createdAt"
    environmentId = "environmentId"
    id = "id"
    status = "status"
    taskType = "taskType"


class SubscriptionMigrationTime(str, Enum):
    END_OF_BILLING_PERIOD = "END_OF_BILLING_PERIOD"
    IMMEDIATE = "IMMEDIATE"


class SubscriptionPriceSortFields(str, Enum):
    billingModel = "billingModel"
    createdAt = "createdAt"
    featureId = "featureId"
    hasSoftLimit = "hasSoftLimit"
    id = "id"
    updatedAt = "updatedAt"
    usageLimit = "usageLimit"


class SubscriptionScheduleStatus(str, Enum):
    Canceled = "Canceled"
    Done = "Done"
    Failed = "Failed"
    PendingPayment = "PendingPayment"
    Scheduled = "Scheduled"


class SubscriptionScheduleType(str, Enum):
    Addon = "Addon"
    BillingPeriod = "BillingPeriod"
    Downgrade = "Downgrade"
    MigrateToLatest = "MigrateToLatest"
    Plan = "Plan"
    UnitAmount = "UnitAmount"


class SubscriptionStartSetup(str, Enum):
    FREE_PLAN = "FREE_PLAN"
    PLAN_SELECTION = "PLAN_SELECTION"
    TRIAL_PERIOD = "TRIAL_PERIOD"


class SubscriptionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CANCELED = "CANCELED"
    EXPIRED = "EXPIRED"
    IN_TRIAL = "IN_TRIAL"
    NOT_STARTED = "NOT_STARTED"
    PAYMENT_PENDING = "PAYMENT_PENDING"


class SyncStatus(str, Enum):
    ERROR = "ERROR"
    NO_SYNC_REQUIRED = "NO_SYNC_REQUIRED"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"


class TaskStatus(str, Enum):
    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    PARTIALLY_FAILED = "PARTIALLY_FAILED"
    PENDING = "PENDING"


class TaskType(str, Enum):
    IMPORT_INTEGRATION_CATALOG = "IMPORT_INTEGRATION_CATALOG"
    IMPORT_INTEGRATION_CUSTOMERS = "IMPORT_INTEGRATION_CUSTOMERS"
    IMPORT_SUBSCRIPTIONS_BULK = "IMPORT_SUBSCRIPTIONS_BULK"
    RECALCULATE_BATCH_ENTITLEMENTS = "RECALCULATE_BATCH_ENTITLEMENTS"
    RECALCULATE_ENTITLEMENTS = "RECALCULATE_ENTITLEMENTS"
    RESYNC_INTEGRATION = "RESYNC_INTEGRATION"
    SUBSCRIPTION_MIGRATION = "SUBSCRIPTION_MIGRATION"
    SUBSCRIPTION_MIGRATION_V2 = "SUBSCRIPTION_MIGRATION_V2"


class TiersMode(str, Enum):
    GRADUATED = "GRADUATED"
    VOLUME = "VOLUME"


class TrialPeriodUnits(str, Enum):
    DAY = "DAY"
    MONTH = "MONTH"


class UnitTransformationRound(str, Enum):
    DOWN = "DOWN"
    UP = "UP"


class UsageMeasurementSortFields(str, Enum):
    createdAt = "createdAt"
    environmentId = "environmentId"
    id = "id"


class UsageUpdateBehavior(str, Enum):
    DELTA = "DELTA"
    SET = "SET"


class VendorIdentifier(str, Enum):
    AWS_MARKETPLACE = "AWS_MARKETPLACE"
    BIG_QUERY = "BIG_QUERY"
    HUBSPOT = "HUBSPOT"
    SALESFORCE = "SALESFORCE"
    SNOWFLAKE = "SNOWFLAKE"
    STRIPE = "STRIPE"
    ZUORA = "ZUORA"


class WeeklyAccordingTo(str, Enum):
    EveryFriday = "EveryFriday"
    EveryMonday = "EveryMonday"
    EverySaturday = "EverySaturday"
    EverySunday = "EverySunday"
    EveryThursday = "EveryThursday"
    EveryTuesday = "EveryTuesday"
    EveryWednesday = "EveryWednesday"
    SubscriptionStart = "SubscriptionStart"


class WidgetType(str, Enum):
    CHECKOUT = "CHECKOUT"
    CUSTOMER_PORTAL = "CUSTOMER_PORTAL"
    PAYWALL = "PAYWALL"


class YearlyAccordingTo(str, Enum):
    SubscriptionStart = "SubscriptionStart"


class experimentGroupType(str, Enum):
    CONTROL = "CONTROL"
    VARIANT = "VARIANT"
