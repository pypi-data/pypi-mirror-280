"""
Reference constants
"""

# Trisomy 21 constants
TRISOMY_21 = "trisomy-21"

# Turner constants
TURNERS = "turners-syndrome"

# UK-WHO constants
UK_WHO = "uk-who"
UK90_PRETERM = "uk90_preterm"
UK_WHO_INFANT = "uk_who_infant"
UK_WHO_CHILD = "uk_who_child"
UK90_CHILD = "uk90_child"
UK_WHO_REFERENCES = [UK90_PRETERM, UK_WHO_INFANT, UK_WHO_CHILD, UK90_CHILD]

# 23 weeks is the lowest decimal age available on the UK90 charts
UK90_REFERENCE_LOWER_THRESHOLD = (
    (23 * 7) - (40 * 7)) / 365.25  # 23 weeks as decimal age

# The WHO references change from measuring infants in the lying position to measuring children in the standing position at 2.0 years.
WHO_CHILD_LOWER_THRESHOLD = 2.0  # 2 years as decimal age
# The UK-WHO standard is complicated because it switches from the WHO references to UK90 references
#  at the age of 4.0 years. This is because it was felt the reference data from breast fed infants
#  from the WHO cohorts were more accurate than the UK90 cohorts for this age group.
#  The Term reference averaged all L, M and S from 37-42 weeks. This is now deprecated and therefore UK90 data is used
# for all measurements across this age range
# Caution is advised when interpreting serial measurements over this time periods - babies are often measured inaccurately and
# up to 10% weight loss is expected in the first 2 weeks of life, and birthweight is often not regained until
# 3 weeks of life

WHO_CHILDREN_UPPER_THRESHOLD = 4.0
UK_WHO_INFANT_LOWER_THRESHOLD = (
    (42 * 7) - (40 * 7)) / 365.25  # 42 weeks as decimal age
UK90_UPPER_THRESHOLD = 20


# Generic constants
MALE="male"
FEMALE="female"
HEIGHT="height"
WEIGHT="weight"
HEAD_CIRCUMFERENCE="ofc"
BMI="bmi"
REFERENCES = [UK_WHO, TRISOMY_21, TURNERS]
SEXES = [MALE, FEMALE]
MEASUREMENT_METHODS = [HEIGHT, WEIGHT, HEAD_CIRCUMFERENCE, BMI]

# Nomenclature
# Centile formats describe the collection - the two most common used are the cole-nine-centiles format used in UK-WHO
# and the three-percent-centiles used by the CDC. They use 5/10/25/50/75/90/95 and suggest 3rd centile 
# is unlikely necessary.

THREE_PERCENT_CENTILES = 'three-percent-centiles'
COLE_TWO_THIRDS_SDS_NINE_CENTILES = 'cole-nine-centiles'
CENTILE_FORMATS=[THREE_PERCENT_CENTILES, COLE_TWO_THIRDS_SDS_NINE_CENTILES]

THREE_PERCENT_CENTILE_COLLECTION = [
    3.0, 5.0, 10.0, 25.0, 50.0, 75.0, 90.0, 95.0, 97.0]
COLE_TWO_THIRDS_SDS_NINE_CENTILE_COLLECTION = [
    0.4, 2.0, 9.0, 25.0, 50.0, 75.0, 91.0, 98.0, 99.6]
