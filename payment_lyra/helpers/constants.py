# coding: utf-8
#
# Copyright © Lyra Network.
# This file is part of Lyra Collect plugin for Odoo. See COPYING.md for license details.
#
# Author:    Lyra Network (https://www.lyra.com)
# Copyright: Copyright © Lyra Network
# License:   http://www.gnu.org/licenses/agpl.html GNU Affero General Public License (AGPL v3)

LYRA_PARAMS = {
    "GATEWAY_CODE": "Lyra",
    "GATEWAY_NAME": "Lyra Collect",
    "BACKOFFICE_NAME": "Lyra Expert",
    "SUPPORT_EMAIL": "support-ecommerce@lyra-collect.com",
    "GATEWAY_URL": "https://secure.lyra.com/vads-payment/",
    "SITE_ID": "12345678",
    "KEY_TEST": "1111111111111111",
    "KEY_PROD": "2222222222222222",
    "CTX_MODE": "TEST",
    "SIGN_ALGO": "SHA-256",
    "LANGUAGE": "en",
    "GATEWAY_VERSION": "V2",
    "PLUGIN_VERSION": "2.0.0",
    "CMS_IDENTIFIER": "Odoo_15",
}

# https://payzen.io/en-EN/form-payment/reference/vads-language.html
LYRA_LANGUAGES = {
    "de": "German",
    "en": "English",
    "cn": "Chinese",
    "es": "Spanish",
    "fr": "French",
    "it": "Italian",
    "ja": "Japanese",
    "nl": "Dutch",
    "pl": "Polish",
    "pt": "Portuguese",
    "ru": "Russian",
    "sv": "Swedish",
    "tr": "Turkish",
}

# values from https://payzen.io/en-EN/form-payment/reference/vads-payment-cards.html
LYRA_CARDS = {
    "ACCORD_STORE": "Accord brand card",
    "ACCORD_STORE_SB": "Accord brand card - Sandbox mode",
    "ALINEA": "Alinéa brand card",
    "ALINEA_CDX": "Alinéa gift card",
    "ALINEA_CDX_SB": "Alinéa gift card - Sandbox mode",
    "ALINEA_SB": "Alinéa brand card - Sandbox mode",
    "ALIPAY": "Alipay",
    "ALLOBEBE_CDX": "Allobébé gift card",
    "ALLOBEBE_CDX_SB": "Allobébé gift card - Sandbox mode",
    "AMEX": "American Express",
    "APETIZ": "Apetiz electronic meal voucher",
    "AUCHAN": "Auchan brand card",
    "AUCHAN_SB": "Auchan brand card - Sandbox mode",
    "AURORE-MULTI": "Cpay card",
    "BANCONTACT": "Bancontact Mistercash",
    "BIZZBEE_CDX": "BizzBee gift card",
    "BIZZBEE_CDX_SB": "BizzBee gift card - Sandbox mode",
    "BOULANGER": "Boulanger brand card",
    "BOULANGER_SB": "Boulanger brand card - Sandbox mode",
    "BRICE_CDX": "Brice gift card",
    "BRICE_CDX_SB": "Brice gift card - Sandbox mode",
    "CB": "CB",
    "CHQ_DEJ": "Chèque Déjeuner electronic meal voucher",
    "CONECS": "Conecs electronic meal voucher",
    "CORA": 'CORA" Aurore card',
    "CORA_BLANCHE": 'CORA Blanche" Aurore card',
    "CORA_PREM": 'CORA Premium" Aurore card',
    "CORA_VISA": 'CORA VISA" Aurore card',
    "CVCO": "Chèque-Vacances Connect",
    "DINERS": "Diners",
    "DISCOVER": "Discover",
    "E_CV": "e-Chèque-Vacances",
    "E-CARTEBLEUE": "e-carte bleue",
    "ECCARD": "Euro-Cheque card",
    "EDENRED_EC": "Edenred Ticket Eco Chèque",
    "EDENRED_SC": "Sports & Culture Edenred Ticket",
    "EDENRED_TC": "Edenred Ticket Compliment",
    "EDENRED_TR": "Edenred meal voucher",
    "FRANFINANCE_3X": "Franfinance payment in 3X",
    "FRANFINANCE_4X": "Franfinance payment in 4X",
    "FULLCB3X": "Payment in 3 installments with no fees with BNPP PF",
    "FULLCB4X": "Payment in 4 installments with no fees with BNPP PF",
    "GIROPAY": "Giropay",
    "GOOGLEPAY": "Google Pay wallet payment",
    "IDEAL": "iDeal Internet Banking",
    "ILLICADO": "Illicado Gift Card",
    "ILLICADO_SB": "JouéClub gift card - Sandbox mode",
    "JCB": "JCB",
    "JOUECLUB_CDX": "Jouéclub gift card",
    "JOUECLUB_CDX_SB": "JouéClub gift card - Sandbox mode",
    "JULES_CDX": "Jules gift card",
    "JULES_CDX_SB": "Jules gift card - Sandbox mode",
    "KLARNA": "Klarna Internet Banking",
    "LEROY-MERLIN": "Leroy-Merlin brand card",
    "LEROY-MERLIN_SB": "Leroy-Merlin brand card - Sandbox mode",
    "MAESTRO": "Maestro",
    "MASTERCARD": "Mastercard",
    "MASTERPASS": "MasterPass",
    "MULTIBANCO": "Multibanco",
    "MYBANK": "MyBank",
    "NORAUTO": "Norauto brand card",
    "NORAUTO_SB": "Norauto brand card - Sandbox mode",
    "ONEY_3X_4X": "Oney 3x 4x payment",
    "ONEY_ENSEIGNE": "Oney partner Brand Cards.",
    "PAYDIREKT": "PayDirekt",
    "PAYLIB": "Wallet Paylib",
    "PAYPAL": "PayPal",
    "PAYPAL_SB": "PayPal - Sandbox mode",
    "PICWIC": "PicWic brand card",
    "PICWIC_SB": "PicWic brand card - Sandbox mode",
    "POSTFINANCE": "PostFinance",
    "POSTFINANCE_EFIN": "PostFinance E-finance",
    "PRESTO": "Presto by Cetelem online credit solution",
    "PRZELEWY24": "Przelewy24",
    "SCT": "SEPA CREDIT TRANSFER",
    "SDD": "SEPA DIRECT DEBIT",
    "SODEXO": "Sodexo electronic meal voucher",
    "SOFORT_BANKING": "Sofort Banking",
    "UNION_PAY": "Union Pay",
    "VILLAVERDE": "Villaverde gift card",
    "VILLAVERDE_SB": "Villaverde gift card - Sandbox mode",
    "VISA": "Visa",
    "VISA_ELECTRON": "Visa Electron",
    "VPAY": "Vpay",
    "WECHAT": "WeChat",
}

# https://payzen.io/en-EN/form-payment/reference/vads-currency.html
LYRA_CURRENCIES = [
    # Argentine Peso
    ["ARS", "032", 2],
    # Australian Dollar
    ["AUD", "036", 2],
    # Cambodian Riel
    ["KHR", "116", 0],
    # Canadian Dollar
    ["CAD", "124", 2],
    # Chinese Yuan (Renminbi)
    ["CNY", "156", 1],
    # Colombian Peso
    ["COP", "170", 2],
    # Czech Crown
    ["CZK", "203", 2],
    # Danish Crown
    ["DKK", "208", 2],
    # Hong Kong Dollar
    ["HKD", "344", 2],
    # Hungarian Forint
    ["HUF", "348", 2],
    # Indian Rupee
    ["INR", "356", 2],
    # Indonesian Rupiah
    ["IDR", "360", 2],
    # Japanese Yen
    ["JPY", "392", 0],
    # South Korean Won
    ["KRW", "410", 0],
    # Kuwaiti Dinar
    ["KWD", "414", 3],
    # Malaysian Ringgit
    ["MYR", "458", 2],
    # Mexican Peso
    ["MXN", "484", 2],
    # Moroccan Dirham
    ["MAD", "504", 2],
    # New Zealand dollar
    ["NZD", "554", 2],
    # Norwegian Crown
    ["NOK", "578", 2],
    # Peruvian Sol
    ["PEN", "604", 2],
    # Philippine Peso
    ["PHP", "608", 2],
    # Russian Ruble
    ["RUB", "643", 2],
    # Singapore Dollar
    ["SGD", "702", 2],
    # South-African Rand
    ["ZAR", "710", 2],
    # Swedish Crown
    ["SEK", "752", 2],
    # Swiss Franc
    ["CHF", "756", 2],
    # Thai Baht
    ["THB", "764", 2],
    # Tunisian Dinar
    ["TND", "788", 3],
    # Pound Sterling
    ["GBP", "826", 2],
    # US Dollar
    ["USD", "840", 2],
    # Taiwan New Dollar
    ["TWD", "901", 2],
    # New Turkish Lira
    ["TRY", "949", 2],
    # West African CFA franc
    ["XOF", "952", 0],
    # CFP Franc
    ["XPF", "953", 0],
    # Euro
    ["EUR", "978", 2],
    # Polish Zloty
    ["PLN", "985", 2],
    # Brazilian Real
    ["BRL", "986", 2],
]
