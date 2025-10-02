from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

LOGIN_PAGE = r"file:///C:/Users/ASUS/Documents/CONG NGHE PHAN MEM/fulllogin.html"

# --- Test Case 1: Đăng nhập thành công ---
def test_login_success():
    driver.get(LOGIN_PAGE)
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("123")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text
    assert "Đăng nhập thành công" in msg
    print("✅ Test 1 Passed: Đăng nhập thành công")

# --- Test Case 2: Sai mật khẩu ---
def test_login_fail_wrong_password():
    driver.get(LOGIN_PAGE)
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text
    assert "Sai tên đăng nhập hoặc mật khẩu" in msg
    print("✅ Test 2 Passed: Sai mật khẩu -> hiển thị thông báo lỗi")

# --- Test Case 3: Bỏ trống trường ---
def test_empty_fields():
    driver.get(LOGIN_PAGE)
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text
    assert "Vui lòng nhập đầy đủ thông tin" in msg
    print("✅ Test 3 Passed: Cảnh báo nhập đầy đủ thông tin")

# --- Test Case 4: Link Quên mật khẩu ---
def test_forgot_password_link():
    driver.get(LOGIN_PAGE)
    forgot_link = driver.find_element(By.ID, "forgotLink")
    assert forgot_link.is_displayed()
    forgot_link.click()
    time.sleep(1)
    assert "forgot.html" in driver.current_url
    print("✅ Test 4 Passed: Link Quên mật khẩu hoạt động")

# --- Test Case 5: Link Đăng ký ---
def test_register_link():
    driver.get(LOGIN_PAGE)
    register_link = driver.find_element(By.ID, "registerLink")
    assert register_link.is_displayed()
    register_link.click()
    time.sleep(1)
    assert "register.html" in driver.current_url
    print("✅ Test 5 Passed: Link Đăng ký hoạt động")

# --- Test Case 6: Social login ---
def test_social_buttons():
    driver.get(LOGIN_PAGE)

    # Facebook
    fb_btn = driver.find_element(By.ID, "fbLogin")
    assert fb_btn.is_displayed()
    fb_btn.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    assert "facebook.com" in driver.current_url.lower()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("✅ Test Social Passed: fbLogin -> facebook.com")

    # Google
    gg_btn = driver.find_element(By.ID, "googleLogin")
    assert gg_btn.is_displayed()
    gg_btn.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    assert "accounts.google.com" in driver.current_url.lower()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("✅ Test Social Passed: googleLogin -> accounts.google.com")

    # Twitter (x.com redirect)
    tw_btn = driver.find_element(By.ID, "twitterLogin")
    assert tw_btn.is_displayed()
    tw_btn.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    current_url = driver.current_url.lower()
    assert "twitter.com" in current_url or "x.com" in current_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("✅ Test Social Passed: twitterLogin -> twitter.com / x.com")

# --- Chạy tất cả test ---
if __name__ == "__main__":
    test_login_success()
    test_login_fail_wrong_password()
    test_empty_fields()
    test_forgot_password_link()
    test_register_link()
    test_social_buttons()
    print("🎉 Tất cả test case đã passed!")
    driver.quit()
