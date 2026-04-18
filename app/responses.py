# -*- coding: utf-8 -*-
"""
Pool of 100 mock responses for Than Nông AI mock service.
- 40 plain text (Latin/no-diacritic Vietnamese)
- 60 rich Markdown with tables, headers, bullets, emojis, bold, italic
All strings are stored as actual UTF-8 text.
"""

# fmt: off
MOCK_RESPONSES: list[str] = [

    # ── PLAIN TEXT (40) ──────────────────────────────────────────────────────

    'Bạn đã check-in lúc 08:02 sáng nay. Chúc bạn làm việc hiệu quả!',
    'Hệ thống ghi nhận bạn check-out lúc 17:35. Thời gian làm việc hôm nay: 9 giờ 33 phút.',
    'Hôm qua bạn chưa check-out. Vui lòng liên hệ HR để điều chỉnh chấm công.',
    'Bạn đã check-in muộn 14 phút so với giờ quy định. Hệ thống đã ghi nhận.',
    'Vị trí check-in của bạn nằm ngoài phạm vi cho phép. Vui lòng check-in trong khu vực công ty.',
    'Thiết bị QR tại cổng A đang hoạt động bình thường. Bạn có thể check-in.',
    'Bạn đang trong ca tăng ca. Thời gian tăng ca hôm nay: 2 giờ 10 phút.',
    'Lịch sử check-in 7 ngày gần nhất của bạn đã được gửi qua email.',
    'Đơn xin nghỉ phép của bạn đã được gửi đến quản lý. Vui lòng chờ phê duyệt.',
    'Quản lý đã duyệt đơn nghỉ phép của bạn từ ngày 25/04 đến 28/04. Chúc bạn nghỉ vui!',
    'Bạn còn 8 ngày phép năm chưa sử dụng trong năm nay.',
    'Đơn xin nghỉ phép bị từ chối do trùng cao điểm. Vui lòng chọn ngày khác.',
    'Đơn nghỉ bệnh đã được ghi nhận. Chúc bạn mau bình phục!',
    'Lương tháng này đã được chuyển khoản vào tài khoản ngân hàng vào ngày 05.',
    'Phiếu lương đã được gửi qua email đăng ký. Vui lòng kiểm tra hộp thư.',
    'Phụ cấp tháng này: ăn trưa 500.000đ, xăng xe 300.000đ.',
    'Bạn có thưởng KPI tháng 3: 2.000.000đ. Đã được cộng vào lương tháng 4.',
    'Đơn hàng #ORD-2026-04182 đã được xác nhận và đang chờ giao.',
    'Sản phẩm bán chạy nhất tháng này đang được phân tích từ dữ liệu POS.',
    'Đơn hàng bị hủy hôm nay: 3 đơn. Lý do chủ yếu: hết hàng.',
    'Đơn hàng online chờ xử lý: 7 đơn. Vui lòng xử lý trong 2 giờ.',
    'Ticket #TKT-1042 đã được tiếp nhận. Thời gian xử lý dự kiến: 24 giờ.',
    'Ticket #TKT-1039 đã được đóng. Vấn đề đã được giải quyết thành công.',
    'Đội hỗ trợ kỹ thuật sẽ liên hệ bạn trong vòng 2 giờ làm việc.',
    'Ticket ưu tiên cao #TKT-1055 đang được xử lý khẩn cấp.',
    'Xin chào! Tôi là Thần Nông AI, trợ lý thông minh của iAttendance. Tôi có thể giúp gì cho bạn?',
    'Tôi đang lắng nghe. Bạn cần hỗ trợ gì về hệ thống iAttendance?',
    'Câu hỏi hay đấy! Để tôi tra cứu thông tin cho bạn nhé.',
    'Tôi hiểu rồi. Dữ liệu đang được xử lý, vui lòng chờ trong giây lát.',
    'Thông tin của bạn đã được ghi nhận thành công.',
    'Cảm ơn bạn đã sử dụng iAttendance! Nếu cần thêm hỗ trợ, hãy hỏi tôi bất cứ lúc nào.',
    'Tôi đã kiểm tra hệ thống. Mọi thứ đang hoạt động bình thường.',
    'Tôi xin lỗi vì sự bất tiện này. Vui lòng mô tả chi tiết hơn để tôi hỗ trợ tốt hơn.',
    'Xin lỗi, tôi chưa hiểu rõ yêu cầu. Bạn có thể diễn đạt lại không?',
    'Dữ liệu bạn cần hiện chưa có trong hệ thống. Vui lòng kiểm tra lại.',
    'Phiên làm việc đã hết hạn. Vui lòng đăng nhập lại để tiếp tục.',
    'Xin lỗi, tôi không có quyền truy cập thông tin này. Vui lòng liên hệ quản trị viên.',
    'Hệ thống đang bảo trì. Vui lòng thử lại sau 15 phút.',
    'Không tìm thấy nhân viên với thông tin bạn cung cấp. Vui lòng kiểm tra lại mã nhân viên.',
    'Lỗi kết nối tạm thời. Hệ thống đã ghi nhận và đang xử lý. Vui lòng thử lại.',

    # ── MARKDOWN (60) ────────────────────────────────────────────────────────

    # Attendance (12)
    '## ✅ Check-in Confirmed\n\n**Nhân viên:** Bạn  \n**Thời gian:** `08:02` sáng nay  \n**Trạng thái:** 🟢 Đúng giờ\n\n---\n> Chúc bạn có một ngày làm việc hiệu quả! 💪',

    '## 📋 Bảng Chấm Công Tuần Này\n\n| Ngày | Check-in | Check-out | Giờ làm |\n|------|----------|-----------|-------|\n| Thứ 2 | 08:01 | 17:02 | 9h01 |\n| Thứ 3 | 07:58 | 17:30 | 9h32 |\n| Thứ 4 | 08:15 | 17:00 | 8h45 |\n| Thứ 5 | 08:00 | 18:10 | 10h10 |\n| Thứ 6 | 08:05 | 17:05 | 9h00 |\n\n**Tổng giờ làm:** `46h28` ⭐  \n**Trạng thái:** ✅ Đủ công tuần này',

    '## ⏰ Nhắc Nhở Check-out\n\n> ⚠️ Bạn **chưa check-out** hôm qua.\n\n**Hành động cần thực hiện:**\n- [ ] Liên hệ HR để điều chỉnh\n- [ ] Cung cấp lý do vắng check-out\n- [ ] Xác nhận giờ rời khỏi thực tế\n\n📧 Email HR: **hr@company.com**',

    '## 📊 Báo Cáo Chấm Công Tháng\n\n| Chỉ số | Giá trị |\n|--------|-------|\n| 📅 Ngày đi làm | **22 ngày** |\n| ✅ Đúng giờ | 20 ngày |\n| ⚠️ Đi muộn | 2 ngày |\n| 🏖️ Nghỉ có phép | 1 ngày |\n| ❌ Vắng không phép | 0 ngày |\n\n**Nhận xét:** _Tháng này bạn làm việc rất chăm chỉ!_ 🎉',

    '## 🏢 Thông Tin Ca Làm Việc\n\n**Ca hiện tại:** Ca sáng  \n**Giờ bắt đầu:** `08:00`  \n**Giờ kết thúc:** `17:00`\n\n---\n\n### ⏳ Tiến độ hôm nay\n- ✅ Check-in lúc `08:05`\n- ⏳ Còn **2 giờ 15 phút** nữa hết ca\n- 🍱 Giờ nghỉ trưa: `12:00 - 13:00`',

    '## 🚨 Cảnh Báo Vị Trí Check-in\n\n> ❌ Vị trí GPS của bạn **nằm ngoài phạm vi** cho phép.\n\n**Phạm vi hợp lệ:** Trong vòng 100m từ cổng  \n**Vị trí của bạn:** Cách cổng ~350m\n\n**Giải pháp:**\n1. Di chuyển vào khu vực công ty\n2. Kết nối WiFi nội bộ\n3. Liên hệ admin nếu bạn làm remote hôm nay',

    '## 👥 Tình Hình Nhân Sự Hôm Nay\n\n| Trạng thái | Số lượng |\n|------------|----------|\n| ✅ Đã check-in | **45** |\n| ⏰ Đi muộn | 3 |\n| ❌ Vắng mặt | 2 |\n| 🏖️ Đang nghỉ phép | 4 |\n| **Tổng** | **54** |\n\n*Cập nhật lúc: 09:00*',

    '## 🌙 Báo Cáo Tăng Ca\n\n**Nhân viên:** Bạn  \n**Ca tăng ca:** Hôm nay sau `17:00`\n\n| Mốc thời gian | Giờ |\n|--------------|-------|\n| Kết thúc ca chính | 17:00 |\n| Bắt đầu tăng ca | 17:05 |\n| **Tổng TG tăng ca** | **2h10** |\n\n> 💰 Phụ cấp tăng ca sẽ được tính vào lương tháng này.',

    '## 🏆 Thành Tích Chuyên Cần\n\n> 🎉 Chúc mừng! Tháng này bạn đạt **chuyên cần 100%**\n\n**Chi tiết:**\n- 📅 Tổng ngày làm việc: **22/22**\n- ⏰ Số lần đúng giờ: **22/22**\n- 🌙 Số ngày tăng ca: 5 ngày\n\n*Thành tích sẽ được ghi nhận trong KPI quý 2.* ⭐',

    '## 📱 Trạng Thái Thiết Bị QR\n\n| Thiết bị | Vị trí | Trạng thái |\n|----------|--------|------------|\n| QR-001 | Cổng chính | 🟢 Online |\n| QR-002 | Cổng phụ | 🟢 Online |\n| QR-003 | Tầng 2 | 🔴 Offline |\n| QR-004 | Tầng 3 | 🟢 Online |\n\n> ⚠️ QR-003 đang có sự cố. Kỹ thuật viên đang xử lý.',

    '## 📈 Thống Kê Check-in 30 Ngày Qua\n\n**Tỷ lệ chuyên cần:** `95.5%` 🟢  \n**Xếp loại:** _Xuất sắc_\n\n| Loại | Số ngày |\n|------|----------|\n| ✅ Đúng giờ | 20 |\n| ⚠️ Đi muộn | 2 |\n| 🏖️ Nghỉ phép | 1 |',

    '## ⏱️ Check-out Thành Công\n\n| | |\n|---|---|\n| 🕔 Giờ check-out | `17:35` |\n| ⏱️ Tổng giờ làm | `9h33` |\n| 📍 Vị trí | Cổng chính |\n| ✅ Trạng thái | Hợp lệ |\n\n---\n*Hẹn gặp lại bạn vào ngày mai! 👋*',

    # Leave (10)
    '## 🏖️ Đơn Nghỉ Phép Đã Duyệt\n\n> ✅ Quản lý **đã phê duyệt** đơn nghỉ phép của bạn\n\n| Thông tin | Chi tiết |\n|-----------|----------|\n| 📅 Từ ngày | 25/04/2026 |\n| 📅 Đến ngày | 28/04/2026 |\n| 🗓️ Số ngày | 4 ngày |\n| 📝 Loại phép | Phép năm |\n\n*Chúc bạn có kỳ nghỉ vui vẻ!* 🌴',

    '## 📊 Tổng Hợp Ngày Phép Năm 2026\n\n| Loại | Tổng | Đã dùng | Còn lại |\n|------|-------|---------|--------|\n| Phép năm | 12 ngày | 4 ngày | **8 ngày** |\n| Phép bệnh | 5 ngày | 0 ngày | **5 ngày** |\n| Phép không lương | Không giới hạn | 0 ngày | - |\n\n> ⚠️ Hạn sử dụng phép năm: **31/12/2026**',

    '## 📝 Trạng Thái Đơn Nghỉ Phép\n\n**Đơn #LEV-2026-0421**\n\n**Trạng thái hiện tại:** Đang chờ quản lý phê duyệt  \n**Thời gian dự kiến:** 1-2 ngày làm việc\n\n> 📧 Bạn sẽ nhận email thông báo khi có cập nhật.',

    '## ❌ Đơn Nghỉ Phép Bị Từ Chối\n\n> ⚠️ Đơn nghỉ phép của bạn **không được duyệt**\n\n**Lý do:** Trùng với thời gian cao điểm cuối tháng\n\n**Gợi ý ngày thay thế:**\n- 05/05 - 07/05 ✅ Khả dụng\n- 12/05 - 14/05 ✅ Khả dụng\n\n*Vui lòng chọn ngày khác và nộp lại đơn.*',

    '## 💊 Nghỉ Bệnh Đã Ghi Nhận\n\n| Thông tin | |\n|-----------|---|\n| 📅 Ngày nghỉ | Hôm nay |\n| 📋 Loại | Nghỉ bệnh |\n| 📄 Giấy tờ | Cần nộp trong 3 ngày |\n\n**Nhắc nhở sau khi đi làm lại:**\n- [ ] Nộp giấy chứng nhận y tế cho HR\n- [ ] Cập nhật lịch công việc với team\n\n*Chúc bạn mau bình phục!* 🌿',

    '## 📅 Lịch Nghỉ Phép Phòng Ban Tuần Này\n\n| Nhân viên | Từ | Đến | Loại |\n|-----------|------|-------|-------|\n| Nguyễn Văn A | 21/04 | 22/04 | Phép năm |\n| Trần Thị B | 22/04 | 22/04 | Phép bệnh |\n| Lê Văn C | 23/04 | 25/04 | Phép năm |\n\n> 📌 Vui lòng phối hợp công việc với các thành viên còn lại.',

    '## ⏰ Nhắc Nhở Phép Năm Chưa Dùng\n\n> 📢 Bạn còn **10 ngày phép** chưa sử dụng!\n\n**Chính sách công ty:**\n- Phép năm **không tích lũy** sang năm sau quá **5 ngày**\n- Hạn cuối sử dụng: `31/12/2026`\n- Phép dư sẽ bị **mất** nếu không đăng ký trước 15/12\n\n*Hãy lên kế hoạch nghỉ ngơi hợp lý nhé!* 🏖️',

    '## 📊 Thống Kê Phép Tháng Này\n\n| Chỉ số | Số liệu |\n|--------|----------|\n| 🏖️ Tổng ngày nghỉ phép | 15 ngày |\n| ✅ Tỷ lệ sử dụng phép | 62% |\n| ⏳ Đơn đang chờ duyệt | 3 đơn |\n| ❌ Đơn bị từ chối | 1 đơn |\n\n*Báo cáo được cập nhật tự động mỗi ngày.*',

    '## 📋 Chính Sách Nghỉ Phép\n\n### 🏖️ Phép năm\n- **12 ngày/năm** cho nhân viên chính thức\n- Tích lũy tối đa **5 ngày** sang năm sau\n\n### 💊 Phép bệnh\n- **5 ngày/năm** được hưởng lương\n- Cần giấy chứng nhận y tế nếu nghỉ ≥ 2 ngày\n\n### 💸 Phép không lương\n- Cần được **Giám đốc** phê duyệt\n- Tối đa **30 ngày/năm**',

    '## ✅ Nghỉ Nửa Ngày Đã Xác Nhận\n\n| | |\n|---|---|\n| 📅 Ngày | Hôm nay |\n| ⏰ Buổi | Chiều (13:00 - 17:00) |\n| 📝 Loại | Phép năm (0.5 ngày) |\n| ✅ Trạng thái | **Đã duyệt** |\n\n*Phép còn lại của bạn: **7.5 ngày*** 🗓️',

    # Payslip (10)
    '## 💰 Bảng Lương Tháng 4/2026\n\n| Khoản mục | Số tiền |\n|-----------|----------|\n| 💵 Lương cơ bản | 15,000,000đ |\n| 🍱 Phụ cấp ăn trưa | 500,000đ |\n| 🛵 Phụ cấp xăng xe | 300,000đ |\n| 🏆 Thưởng KPI | 2,000,000đ |\n| ➖ BHXH (8%) | -1,200,000đ |\n| ➖ Thuế TNCN | -750,000đ |\n| **💳 Thực lĩnh** | **15,850,000đ** |\n\n> 📅 Ngày chuyển khoản: **05/05/2026**',

    '## 📊 Lịch Sử Lương 6 Tháng Gần Nhất\n\n| Tháng | Lương Net | Thưởng | Ghi chú |\n|-------|-----------|--------|----------|\n| T11/2025 | 14,200,000đ | - | |\n| T12/2025 | 14,200,000đ | 5,000,000đ | Thưởng Tết |\n| T01/2026 | 14,500,000đ | - | Tăng lương |\n| T03/2026 | 14,500,000đ | 2,000,000đ | KPI Q1 |\n| **T04/2026** | **15,850,000đ** | 2,000,000đ | KPI tháng 3 |',

    '## 🏆 Thưởng KPI Tháng 3/2026\n\n> 🎉 Chúc mừng! Bạn đã đạt **KPI tháng 3**\n\n| Chỉ tiêu | Mục tiêu | Thực tế | % Đạt |\n|----------|---------|---------|--------|\n| Doanh số | 100tr | 115tr | 115% |\n| Chuyên cần | 95% | 100% | 105% |\n| Chất lượng | 90% | 92% | 102% |\n\n**Thưởng:** `2,000,000đ` 💰  \n*Đã cộng vào lương tháng 4.*',

    '## 📉 So Sánh Lương Tháng Này vs Tháng Trước\n\n| Khoản mục | Tháng 3 | Tháng 4 | Thay đổi |\n|-----------|---------|---------|----------|\n| Lương cơ bản | 14,500k | 15,000k | 🔼 +500k |\n| Phụ cấp | 800k | 1,000k | 🔼 +200k |\n| Thưởng | 2,000k | 2,000k | = |\n| Khấu trừ | -1,800k | -2,150k | 🔽 -350k |\n| **Thực lĩnh** | **15,500k** | **15,850k** | **🔼 +350k** |',

    '## 🏦 Bảo Hiểm Xã Hội Tháng Này\n\n| Loại bảo hiểm | Tỷ lệ NLĐ | Số tiền |\n|---------------|-----------|----------|\n| BHXH | 8% | 1,200,000đ |\n| BHYT | 1.5% | 225,000đ |\n| BHTN | 1% | 150,000đ |\n| **Tổng khấu trừ** | **10.5%** | **1,575,000đ** |\n\n> 📋 Mã số BHXH của bạn: `VN-2026-xxxxx`',

    '## 📈 Thuế Thu Nhập Cá Nhân\n\n**Thu nhập tính thuế tháng này:** `12,275,000đ`\n\n| Bậc thuế | Thu nhập | Thuế suất | Số thuế |\n|----------|---------|-----------|----------|\n| Bậc 1 | 5,000,000đ | 5% | 250,000đ |\n| Bậc 2 | 5,000,000đ | 10% | 500,000đ |\n\n**Tổng thuế TNCN:** `750,000đ`',

    '## 🎁 Chi Tiết Phụ Cấp Tháng 4\n\n| Phụ cấp | Điều kiện | Số tiền |\n|---------|-----------|----------|\n| 🍱 Ăn trưa | Đi làm đủ ngày | 500,000đ |\n| 🛵 Xăng xe | Mặc định | 300,000đ |\n| 📱 Điện thoại | Bộ phận kinh doanh | 200,000đ |\n| 🏠 Nhà ở | Nhân viên ngoại tỉnh | - |\n\n**Tổng phụ cấp:** `1,000,000đ` ✅',

    '## 📋 Phiếu Lương Đã Gởi\n\n> 📧 Phiếu lương tháng 4/2026 đã được gởi đến email của bạn\n\n**Nội dung phiếu lương:**\n- ✅ Chi tiết thu nhập\n- ✅ Các khoản khấu trừ\n- ✅ Thực lĩnh\n- ✅ Mã QR xác minh\n\n*Kiểm tra thư mục Spam nếu không thấy email.* 📬',

    '## 🏦 Thông Tin Tài Khoản Ngân Hàng\n\n| Thông tin | Chi tiết |\n|-----------|----------|\n| 🏦 Ngân hàng | Vietcombank |\n| 💳 Số tài khoản | `........3456` |\n| 👤 Chủ tài khoản | Nguyễn Văn A |\n| ✅ Trạng thái | Đã xác minh |\n\n> 💡 Để thay đổi tài khoản, liên hệ phòng Kế toán trước ngày 25 hàng tháng.',

    '## 📊 Tổng Chi Phí Lương Phòng Ban Tháng 4\n\n| Phòng ban | Nhân sự | Tổng lương |\n|-----------|---------|-------------|\n| Kinh doanh | 8 người | 142,000,000đ |\n| Kỹ thuật | 6 người | 118,000,000đ |\n| Hành chính | 4 người | 68,000,000đ |\n| **Tổng** | **18 người** | **328,000,000đ** |\n\n*Đã được xuất báo cáo cho Kế toán.* 📑',

    # Orders & Revenue (8)
    '## 📦 Chi Tiết Đơn Hàng\n\n**Mã đơn:** `#ORD-2026-04182`\n\n| Thông tin | Chi tiết |\n|-----------|----------|\n| 📅 Ngày đặt | 18/04/2026 |\n| 👤 Khách hàng | Công ty ABC |\n| 💰 Giá trị | 8,500,000đ |\n| 🚚 Trạng thái | Đang giao hàng |\n| ⏱️ Dự kiến giao | 20/04/2026 |',

    '## 📈 Báo Cáo Doanh Thu Tháng Này\n\n| Kênh bán | Doanh thu | % Tổng |\n|----------|-----------|--------|\n| 🏪 Cửa hàng | 125,000,000đ | 55% |\n| 🌐 Online | 65,000,000đ | 29% |\n| 📞 Điện thoại | 36,000,000đ | 16% |\n| **Tổng** | **226,000,000đ** | **100%** |\n\n📊 Tăng **12%** so với cùng kỳ năm ngoái 🔼',

    '## 🏆 Top 5 Sản Phẩm Bán Chạy\n\n| # | Sản phẩm | Số lượng | Doanh thu |\n|---|----------|---------|----------|\n| 🥇 | Gạo ST25 5kg | 342 | 18,500,000đ |\n| 🥈 | Rau cải hữu cơ | 289 | 8,700,000đ |\n| 🥉 | Trứng gà sạch | 256 | 6,400,000đ |\n| 4 | Cà chua bi | 198 | 4,950,000đ |\n| 5 | Thịt heo sạch | 145 | 18,850,000đ |',

    '## 📊 Tóm Tắt Đơn Hàng Tuần 16\n\n> 📅 Tuần 16 (14/04 - 18/04/2026)\n\n| Chỉ số | Số liệu |\n|--------|----------|\n| 📦 Tổng đơn | **142** |\n| ✅ Hoàn thành | 134 (94%) |\n| ❌ Đã hủy | 3 (2%) |\n| ⏳ Đang xử lý | 5 (4%) |\n\n**Giá trị trung bình/đơn:** `1,590,000đ`',

    '## 👥 Phân Tích Khách Hàng Tháng Này\n\n| Phân khúc | Số lượng | Doanh thu |\n|-----------|---------|----------|\n| 🆕 Khách mới | 28 | 42,000,000đ |\n| 🔄 Khách quay lại | 115 | 184,000,000đ |\n| ⭐ Khách VIP | 12 | 98,000,000đ |\n\n**Tỷ lệ giữ chân khách hàng:** `82%` 💚',

    '## ⚡ Đơn Hàng Online Cần Xử Lý\n\n> ⏰ Có **7 đơn** đang chờ - Vui lòng xử lý trong **2 giờ**\n\n| Đơn hàng | Khách | Giá trị | Thời gian chờ |\n|----------|-------|---------|----------------|\n| #4521 | Trần Thị A | 2,300,000đ | 45 phút |\n| #4522 | Lê Văn B | 890,000đ | 1 giờ |\n| #4523 | Phạm Thị C | 5,100,000đ | 1h30 |\n\n*+ 4 đơn khác...*',

    '## 📦 Tồn Kho Cảnh Báo\n\n> 🔴 Một số sản phẩm **sắp hết hàng!**\n\n| Sản phẩm | Tồn kho | Mức tối thiểu | Trạng thái |\n|----------|---------|--------------|------------|\n| Gạo ST25 5kg | 12 túi | 50 túi | 🔴 Nguy hiểm |\n| Rau cải organic | 8 bó | 30 bó | 🔴 Nguy hiểm |\n| Trứng gà sạch | 45 hộp | 100 hộp | 🟡 Thấp |\n\n*Vui lòng liên hệ nhà cung cấp để nhập thêm hàng.*',

    '## 📉 Phân Tích Đơn Hàng Bị Hủy\n\n**Hôm nay có 3 đơn bị hủy:**\n\n| Lý do | Số đơn | % |\n|-------|--------|---|\n| ❌ Hết hàng | 2 | 67% |\n| 💸 Khách hủy | 1 | 33% |\n\n> 💡 Đề xuất: Cập nhật tồn kho và thông báo cho khách hàng chờ.',

    # Farm (8)
    '## 🌾 Báo Cáo Mùa Vụ Tháng Này\n\n| Khu vực | Diện tích | Trạng thái | Sản lượng dự kiến |\n|---------|-----------|------------|-------------------|\n| Khu A | 2.5 ha | 🟢 Tốt | 3,200 kg |\n| Khu B | 1.8 ha | 🟡 Cần chú ý | 1,900 kg |\n| Khu C | 3.0 ha | 🔴 Có sâu bệnh | 2,100 kg |\n\n**Tổng sản lượng dự kiến:** `7,200 kg` 🌱',

    '## 💧 Lịch Tưới Nước Tuần Tới\n\n| Ngày | Khu vực | Giờ | Lượng nước |\n|------|---------|-------|-------------|\n| T2 | Khu A, B | 06:00 | 500 lít |\n| T3 | Khu C | 06:00 | 750 lít |\n| T4 | Khu A | 06:00 | 500 lít |\n| T5 | Khu B, C | 06:00 | 1,000 lít |\n| T6 | Tất cả | 06:00 | 1,500 lít |\n\n> 💡 Thiết bị tưới tự động đã được cài đặt theo lịch.',

    '## 🐛 Cảnh Báo Sâu Bệnh\n\n> ⚠️ Phát hiện dấu hiệu sâu bệnh tại **Khu C**\n\n**Mức độ:** 🟡 Trung bình  \n**Diện tích ảnh hưởng:** ~0.5 ha\n\n**Khuyến nghị:**\n1. Kiểm tra thực địa ngay hôm nay\n2. Phun thuốc trừ sâu sinh học\n3. Báo cáo kết quả sau 48 giờ\n\n📞 Hotline kỹ thuật: `1800-xxxx`',

    '## 🌿 Nhật Ký Nông Trại Hôm Nay\n\n**Thời tiết:** ⛅ Có mây, 28°C\n\n| Hoạt động | Khu vực | Nhân viên | Trạng thái |\n|-----------|---------|-----------|------------|\n| Tưới nước | Khu A | Nguyễn V.A | ✅ Hoàn thành |\n| Bón phân | Khu B | Trần T.B | ✅ Hoàn thành |\n| Kiểm tra sâu | Khu C | Lê V.C | ⏳ Đang làm |\n| Thu hoạch | Khu A | Team 3 | ⏳ Đang làm |',

    '## 📊 Dự Báo Thu Hoạch Tuần Tới\n\n> 🗓️ Tuần 17 (21/04 - 25/04/2026)\n\n| Sản phẩm | Khu vực | Sản lượng dự kiến |\n|----------|---------|-------------------|\n| 🥬 Rau xanh | Khu A | 2.5 tấn |\n| 🍅 Cà chua | Khu B | 800 kg |\n| 🥦 Bông cải | Khu A | 400 kg |\n| 🌽 Ngô | Khu C | 1.2 tấn |\n\n**Tổng dự kiến:** `~5 tấn` 📦',

    '## 🌡️ Giám Sát Môi Trường Nông Trại\n\n| Cảm biến | Vị trí | Giá trị | Trạng thái |\n|----------|--------|---------|------------|\n| 💧 Độ ẩm đất | Khu A | 68% | 🟢 Tối ưu |\n| 💧 Độ ẩm đất | Khu B | 42% | 🟡 Cần tưới |\n| 🌡️ Nhiệt độ | Ngoài trời | 28°C | 🟢 Bình thường |\n| ☀️ UV Index | - | 6 | 🟡 Cao |\n\n*Cập nhật mỗi 30 phút.*',

    '## 🌱 Kế Hoạch Trồng Trọt Tháng 5\n\n| Cây trồng | Khu vực | Ngày trồng | Thu hoạch dự kiến |\n|-----------|---------|-----------|-------------------|\n| Rau muống | Khu A | 01/05 | 15/05 |\n| Cà chua | Khu B | 03/05 | 03/07 |\n| Dưa leo | Khu C | 05/05 | 25/06 |\n| Bắp cải | Khu A | 10/05 | 10/07 |\n\n> 📋 Kế hoạch đã được phê duyệt bởi Kỹ sư nông nghiệp.',

    '## 🚜 Thiết Bị Nông Trại\n\n| Thiết bị | Trạng thái | Bảo dưỡng lần cuối | Lần tới |\n|----------|------------|------------------|---------|\n| Máy tưới tự động | 🟢 Hoạt động | 01/03/2026 | 01/06/2026 |\n| Máy cày | 🟢 Hoạt động | 15/02/2026 | 15/05/2026 |\n| Drone phun thuốc | 🔴 Bảo dưỡng | 10/04/2026 | 25/04/2026 |\n| Tưới nhỏ giọt | 🟢 Hoạt động | 20/03/2026 | 20/06/2026 |',

    # Support, Visitors & General (12)
    '## 🎫 Chi Tiết Ticket Hỗ Trợ\n\n**Ticket:** `#TKT-1042`\n\n| Thông tin | Chi tiết |\n|-----------|----------|\n| 📋 Tiêu đề | Lỗi thiết bị QR cổng B |\n| 🔴 Ưu tiên | Cao |\n| 👤 Người tạo | Nguyễn Văn A |\n| 📅 Ngày tạo | 18/04/2026 |\n| ⏱️ SLA | 4 giờ |\n| 🔄 Trạng thái | Đang xử lý |',

    '## 📊 Hiệu Suất Hỗ Trợ Tháng Này\n\n| Chỉ số | Mục tiêu | Thực tế | Đánh giá |\n|--------|---------|---------|----------|\n| ✅ Giải quyết trong SLA | 95% | **98%** | 🟢 Vượt |\n| ⭐ Điểm hài lòng | 4.0 | **4.6** | 🟢 Vượt |\n| ⏱️ Thời gian xử lý TB | < 6h | **4.2h** | 🟢 Vượt |\n\n*Tháng xuất sắc! Tiếp tục phát huy.* 🏆',

    '## 🖥️ Danh Sách Tài Sản Của Bạn\n\n| Tài sản | Mã | Tình trạng | Bảo hành đến |\n|---------|-----|------------|---------------|\n| 💻 Laptop Dell XPS | ASS-0023 | 🟢 Tốt | 08/2026 |\n| 🖥️ Màn hình phụ | ASS-0091 | 🟢 Tốt | 12/2027 |\n| 📱 Điện thoại công ty | PHN-012 | 🟢 Tốt | 03/2027 |\n| 🪑 Ghế ergonomic | ASS-0145 | 🟡 Cũ | - |',

    '## 🏢 Thông Tin Khách Thăm Hôm Nay\n\n| STT | Khách | Công ty | Gặp | Giờ vào | Trạng thái |\n|-----|-------|---------|------|---------|------------|\n| 1 | Nguyễn T.A | ABC Corp | Marketing | 10:15 | ✅ Trong tòa |\n| 2 | Trần V.B | XYZ Ltd | Giám đốc | 11:00 | ✅ Trong tòa |\n| 3 | Lê T.C | DEF Co | IT | 14:00 | 📅 Hẹn trước |\n\n**Tổng lượt khách hôm nay:** `12` 👥',

    '## ⭐ Feedback Khách Hàng\n\n> 🎉 Bạn vừa nhận được đánh giá **5 sao** từ khách hàng!\n\n> *"Dịch vụ rất tốt, nhân viên nhiệt tình và chuyên nghiệp. Sẽ tiếp tục hợp tác lâu dài!"*\n> — Khách hàng Công ty ABC\n\n| ⭐⭐⭐⭐⭐ | Rất hài lòng |\n|---|---|',

    '## 🎉 Chào Mừng Bạn Đến Với iAttendance AI!\n\n> 🤖 Tôi là **Thần Nông AI** — trợ lý thông minh của iAttendance\n\n### Tôi có thể giúp bạn:\n| Chức năng | Mô tả |\n|-----------|-------|\n| 📋 Chấm công | Tra cứu, báo cáo, xử lý vắng mặt |\n| 🏖️ Nghỉ phép | Nộp đơn, theo dõi trạng thái |\n| 💰 Lương thưởng | Xem phiếu lương, tra cứu KPI |\n| 📦 Đơn hàng | Theo dõi, báo cáo doanh thu |\n| 🌾 Nông trại | Lịch tưới, giám sát môi trường |\n\n*Hãy hỏi tôi bất cứ điều gì!* 😊',

    '## 📅 Lịch Đi Làm Tháng Này\n\n| Tuần | Ngày làm | Ngày nghỉ | Ghi chú |\n|------|---------|-----------|----------|\n| Tuần 14 | 5 ngày | 0 | |\n| Tuần 15 | 5 ngày | 0 | |\n| Tuần 16 | 4 ngày | 1 | Nghỉ phép T6 |\n| Tuần 17 | 5 ngày | 0 | |\n\n**Tổng:** 19/22 ngày làm việc 📅',

    '## 🤖 Hướng Dẫn Sử Dụng Chat AI\n\n**Các lệnh hữu ích:**\n\n| Lệnh | Mô tả |\n|------|-------|\n| `check-in` | Xem trạng thái chấm công |\n| `nghi phep` | Quản lý đơn nghỉ phép |\n| `luong` | Xem phiếu lương |\n| `don hang` | Theo dõi đơn hàng |\n| `bao cao` | Báo cáo tổng hợp |\n\n*Gõ bất kỳ câu hỏi bằng tiếng Việt hoặc tiếng Anh!* 🤖',

    '## 🚧 Thông Báo Bảo Dưỡng Hệ Thống\n\n> ⚠️ Hệ thống iAttendance sẽ **bảo trì** trong thời gian sau:\n\n| Thông tin | Chi tiết |\n|-----------|----------|\n| 📅 Ngày | 20/04/2026 |\n| ⏰ Thời gian | 23:00 - 01:00 |\n| ⏱️ Dự kiến | 2 giờ |\n| ❌ Ảnh hưởng | Check-in QR, API |\n\n*Vui lòng check-in trước 23:00.* 🔧',

    '## 📋 Tóm Tắt Hoạt Động Tuần Này\n\n| Hạng mục | Kết quả |\n|-----------|----------|\n| ✅ Chấm công đầy đủ | 4/5 ngày |\n| 📦 Đơn hàng xử lý | 38 đơn |\n| 🎫 Ticket hỗ trợ | 5 ticket |\n| 📊 Doanh thu | 56,000,000đ |\n\n**Đánh giá tuần:** 🟢 Tốt  \n*Tiếp tục duy trì!* 💪',

    '## 🔍 Tìm Kiếm Nhân Viên\n\n**Kết quả tìm kiếm:** `Nguyễn Văn`\n\n| Nhân viên | Mã NV | Phòng ban | Trạng thái |\n|-----------|--------|-----------|------------|\n| Nguyễn Văn A | NV001 | Kinh doanh | 🟢 Đi làm |\n| Nguyễn Văn B | NV045 | Kỹ thuật | 🟢 Đi làm |\n| Nguyễn Văn C | NV078 | Hành chính | 🏖️ Nghỉ phép |\n\n*3 kết quả được tìm thấy.*',

    '## 📰 Cập Nhật Hệ Thống\n\n> 🆕 **iAttendance v2.5** vừa được cập nhật!\n\n**Tính năng mới:**\n- 🤗 AI chatbot cải tiến\n- 📱 Ứng dụng mobile nâng cấp\n- 📊 Báo cáo thông minh hơn\n- 🔐 Bảo mật 2 lớp (2FA)\n\n*Cập nhật lúc: 15/04/2026 01:00* ✅',
]

