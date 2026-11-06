from pathlib import Path

import pytest 
from playwright.sync_api import Page, expect

PRACTICE_PAGE = Path (__file__).parent/"locaters_practice.html"


@pytest.fixture
def store(page:Page)-> Page:
    page.goto(PRACTICE_PAGE.as_uri())
    return page


def test_css_selectors(store: Page):
    expect(store.locator("header h1")).to_have_text("Practice Store")
    expect(store.locator('input[type="email"]')).to_have_attribute("type", "email")
    expect(store.locator('input[type="password"]')).to_have_attribute("placeholder", "Enter password")
    expect(store.locator("#remember")).not_to_be_checked()
    expect(store.locator('button[type="submit"]')).to_have_text("Sign in")
    expect(store.locator('img[alt="Practice Store logo"]')).to_have_attribute("src", "logo.png")
    expect(store.locator("nav a")).to_have_text(["Home", "Products", "Contact us"])
    expect(store.locator('[title*="shipping"]')).to_have_attribute("title", "Free shipping on orders over $50")
    expect(store.locator('[data-testid="checkout-button"]')).to_have_text("Checkout")
    expect(store.locator("li.product")).to_have_count(4)
    expect(store.locator(".product .price")).to_have_text(["$29.99", "$9.99", "$15.99", "$49.99"])
    expect(store.locator(".product button:disabled")).to_be_disabled()
    expect(store.locator(".product button:not(:disabled)")).to_have_count(3)
    expect(store.locator("li.product:first-child h3")).to_have_text("Backpack")



def  test_xpath_selectors(store:Page):
    expect(store.locator("(//nav//a)[3]")).to_have_text("Contact us")
    expect(store.locator('//input[@id="password"]')).to_have_attribute("type", "password")
    expect(store.locator('//input[@placeholder="you@example.com"]')).to_be_empty()
    expect(store.locator('//a[text()="Home"]')).to_have_attribute("href", "#home")
    expect(store.locator('//a[contains(.,"Forgot")]')).to_have_text("Forgot password?")
    expect(store.locator('//button[text()="Sign in"]')).to_have_attribute("type", "submit")
    expect(store.locator('//label[contains(., "Remember me")]//input[@type="checkbox"]')).to_have_id("remember")
    expect(store.locator('//button[text()="Checkout"]')).to_have_attribute("data-testid", "checkout-button")
    expect(store.locator('//li[@class="product"]')).to_have_count(4)
    expect(store.locator('//h3[text()="Jacket"]')).to_be_visible()
    expect(store.locator('//h3[text()="Bike Light"]/following-sibling::p[@class="price"]')).to_have_text("$9.99")
    expect(store.locator('//p[text()="Out of stock"]/parent::li/h3')).to_have_text("Bike Light")
    expect(store.locator('//li[h3="T-Shirt"]/button')).to_be_enabled()
    expect(store.locator('//button[@disabled]')).to_have_count(1)
    expect(store.locator('(//li[@class="product"]/h3)[2]')).to_have_text("Bike Light")
    