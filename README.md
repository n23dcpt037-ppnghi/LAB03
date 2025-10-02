📝 Test Tự Động - Chức năng Đăng nhập

## 📌 Giới thiệu
Dự án này sử dụng **Selenium + Python** để kiểm thử chức năng **Đăng nhập** trong hệ thống.

## Cấu trúc
- `login_test.py` : File chứa các test case
- `requirements.txt` : Thư viện cần cài đặt
- `fulllogin.html` : Giao diện đăng nhập để test
- `screenshot/` : Thư mục chứa ảnh chụp màn hình kết quả test

## Danh sách Test Case
| STT | Tên Test Case              | Mô tả kiểm thử                                      | Kết quả mong đợi |
|-----|-----------------------------|------------------------------------------------------|------------------|
| 1   | Đăng nhập thành công        | Nhập `username=admin`, `password=123`                | Hiển thị thông báo "Đăng nhập thành công" |
| 2   | Sai mật khẩu                | Nhập đúng username nhưng sai password                | Hiển thị thông báo "Sai tên đăng nhập hoặc mật khẩu" |
| 3   | Bỏ trống trường             | Không nhập username/password, nhấn nút Đăng nhập     | Hiển thị cảnh báo "Vui lòng nhập đầy đủ thông tin" |
| 4   | Link Quên mật khẩu          | Nhấn vào liên kết **Quên mật khẩu**                  | Chuyển sang trang `forgot.html` |
| 5   | Link Đăng ký                | Nhấn vào liên kết **Đăng ký**                        | Chuyển sang trang `register.html` |
| 6   | Đăng nhập mạng xã hội       | Nhấn vào nút Facebook / Google / Twitter             | Mở trang đăng nhập tương ứng (facebook.com / google.com / twitter.com)|

## Cài đặt
1. Cài đặt Python (>=3.8)  
2. Cài đặt thư viện:
   ```bash
   pip install selenium

* Đảm bảo đã cài đặt Chrome và ChromeDriver (phù hợp với version Chrome đang dùng).

## Chạy test
* Trong thư mục dự án, chạy:

```bash
python selenium_login_test.py

```

* Nếu tất cả test case pass, bạn sẽ thấy log tương tự:

✅ Test 1 Passed: Đăng nhập thành công

✅ Test 2 Passed: Sai mật khẩu -> hiển thị thông báo lỗi

✅ Test 3 Passed: Cảnh báo nhập đầy đủ thông tin

✅ Test 4 Passed: Link Quên mật khẩu hoạt động

✅ Test 5 Passed: Link Đăng ký hoạt động

✅ Test Social Passed: fbLogin -> facebook.com

✅ Test Social Passed: googleLogin -> accounts.google.com

✅ Test Social Passed: twitterLogin -> twitter.com / x.com

🎉 Tất cả test case đã passed!

## Kết quả

![test](https://github.com/n23dcpt037-ppnghi/n23dcpt037-phgngi/blob/main/test-report_screenshot/test_login.png?raw=true)

## Thông tin sinh viên
Họ tên: Phan Phương Nghi

MSSV: N23DCPT037

Lớp: D23CQPTTK01-N
