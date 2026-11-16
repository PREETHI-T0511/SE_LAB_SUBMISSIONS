import pytest
from car_insurance_premium import annual_premium, no_claim_bonus, claim_payout


# Annual premium tests

def test_invalid_car():
    with pytest.raises(ValueError):
        annual_premium("truck", 30, 0, False)


def test_underage_driver():
    with pytest.raises(ValueError):
        annual_premium("sedan", 17, 0, False)


def test_young_driver():
    assert annual_premium("hatchback", 22, 1, False) == 12000


def test_middle_aged_driver():
    assert annual_premium("sedan", 35, 1, False) == 12000


def test_senior_driver():
    assert annual_premium("suv", 65, 1, False) == 17000


def test_no_claims():
    assert annual_premium("sedan", 30, 0, False) == 9600


def test_many_claims():
    assert annual_premium("sedan", 35, 3, False) == 24000


def test_anti_theft():
    assert annual_premium("sedan", 35, 1, True) == 11500


# No claim bonus tests

def test_negative_years():
    with pytest.raises(ValueError):
        no_claim_bonus(-1)


def test_zero_years():
    assert no_claim_bonus(0) == 0


def test_one_year():
    assert no_claim_bonus(1) == 20


def test_three_years():
    assert no_claim_bonus(3) == 35


def test_five_years():
    assert no_claim_bonus(5) == 50


# Claim payout tests

def test_negative_damage():
    with pytest.raises(ValueError):
        claim_payout(-100, 50000, 1000, False)


def test_negative_deductible():
    with pytest.raises(ValueError):
        claim_payout(10000, 50000, -1000, False)


def test_total_loss():
    assert claim_payout(60000, 50000, 1000, True) == 50000


def test_damage_below_deductible():
    assert claim_payout(500, 50000, 1000, False) == 0


def test_damage_equal_deductible():
    assert claim_payout(1000, 50000, 1000, False) == 0


def test_exceeds_insured_value():
    assert claim_payout(60000, 50000, 1000, False) == 50000


def test_normal_payout():
    assert claim_payout(10000, 50000, 1000, False) == 9000
