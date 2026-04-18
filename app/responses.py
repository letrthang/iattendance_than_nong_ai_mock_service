"""
Pool of 100 pre-written mock responses for the Thần Nông AI mock service.
Covers iAttendance domains: attendance, leave, payslip, orders, farm, support, assets, visitors, greetings, errors.
"""

MOCK_RESPONSES: list[str] = [
    # ── Attendance / Check-in / Check-out (15) ──────────────────────────────
    "Bạn đã check-in lúc 08:02 sáng nay. Mọi thứ đều ổn, chúc bạn làm việc hiệu quả! 🟢",
    "Hệ thống ghi nhận bạn check-out lúc 17:35. Thời gian làm việc hôm nay: 9 giờ 33 phút.",
    "Trong tuần này bạn đã đi làm đủ 5/5 ngày. Tuyệt vời! 🎉",
    "Hôm qua bạn chưa check-out. Vui lòng liên hệ HR để điều chỉnh chấm công.",
    "Bảng chấm công tháng này của bạn: 22 ngày đi làm, 1 ngày vắng có phép, 0 ngày vắng không phép.",
    "Ca làm việc của bạn hôm nay: 08:00 – 17:00. Còn 2 giờ 15 phút nữa là hết ca.",
    "Bạn đã check-in muộn 14 phút so với giờ quy định. Hệ thống đã ghi nhận.",
    "Vị trí check-in của bạn nằm ngoài phạm vi cho phép. Vui lòng check-in trong khu vực công ty.",
    "Thiết bị QR tại cổng A đang hoạt động bình thường. Bạn có thể check-in.",
    "Dữ liệu chấm công của toàn bộ nhân viên hôm nay: 45/48 đã check-in, 3 chưa có mặt.",
    "Bạn đang trong ca tăng ca. Thời gian tăng ca hôm nay: 2 giờ 10 phút.",
    "Lịch sử check-in 7 ngày gần nhất của bạn đã được gửi qua email.",
    "Hệ thống phát hiện bạn check-in 3 lần liên tiếp sớm hơn 30 phút. Rất chăm chỉ! ⭐",
    "Nhân viên Nguyễn Văn A chưa check-in. Hệ thống đã gửi thông báo nhắc nhở.",
    "Báo cáo chấm công tháng trước đã được xuất và gửi cho quản lý.",

    # ── Leave Management (12) ────────────────────────────────────────────────
    "Đơn xin nghỉ phép của bạn đã được gửi đến quản lý. Vui lòng chờ phê duyệt.",
    "Quản lý đã duyệt đơn nghỉ phép của bạn từ ngày 25/04 đến 28/04. Chúc bạn nghỉ vui! 🏖️",
    "Bạn còn 8 ngày phép năm chưa sử dụng trong năm nay.",
    "Đơn xin nghỉ phép của bạn đã bị từ chối do trùng với thời gian cao điểm. Vui lòng chọn ngày khác.",
    "Chính sách nghỉ phép công ty: 12 ngày phép/năm, tích lũy tối đa 5 ngày sang năm sau.",
    "Danh sách nhân viên đang nghỉ phép tuần này: 3 người. Vui lòng kiểm tra lịch nhóm.",
    "Đơn nghỉ bệnh của bạn đã được ghi nhận. Chúc bạn mau bình phục! 💊",
    "Bạn cần nộp giấy chứng nhận y tế trong vòng 3 ngày làm việc sau khi đi làm trở lại.",
    "Tổng số ngày nghỉ phép của phòng ban tháng này: 15 ngày. Tỷ lệ sử dụng phép: 62%.",
    "Nhắc nhở: Bạn còn 10 ngày phép năm chưa dùng. Hạn cuối sử dụng: 31/12.",
    "Đơn xin nghỉ nửa ngày buổi chiều của bạn đã được ghi nhận.",
    "Quản lý yêu cầu thêm thông tin cho đơn nghỉ phép. Vui lòng kiểm tra email.",

    # ── Payslip & Salary (10) ────────────────────────────────────────────────
    "Bảng lương tháng 4/2026 của bạn đã sẵn sàng. Tổng lương net: được hiển thị trong mục Bảng lương.",
    "Lương tháng này đã được chuyển khoản vào tài khoản ngân hàng của bạn vào ngày 05.",
    "Phụ cấp tháng này: Phụ cấp ăn trưa 500.000đ, phụ cấp xăng xe 300.000đ.",
    "Thuế TNCN tháng này của bạn: được tính tự động theo biểu thuế lũy tiến hiện hành.",
    "Bảo hiểm xã hội tháng này đã được khấu trừ theo quy định (8% lương cơ bản).",
    "Bạn có thưởng KPI tháng 3: 2.000.000đ. Đã được cộng vào lương tháng 4.",
    "Lịch sử bảng lương 6 tháng gần nhất có thể xem tại mục Tài chính → Bảng lương.",
    "Thông tin ngân hàng của bạn đã được cập nhật thành công. Lương tháng sau sẽ chuyển vào tài khoản mới.",
    "Phiếu lương của bạn đã được gửi qua email đăng ký. Vui lòng kiểm tra hộp thư.",
    "Tổng chi phí lương phòng ban tháng này: đã được xuất báo cáo cho kế toán.",

    # ── Orders & Revenue (10) ────────────────────────────────────────────────
    "Doanh thu hôm nay của cửa hàng: đang được tổng hợp theo thời gian thực.",
    "Đơn hàng #ORD-2026-04182 đã được xác nhận và đang chờ giao.",
    "Tổng số đơn hàng trong tuần: 142 đơn. Tỷ lệ hoàn thành: 94%.",
    "Sản phẩm bán chạy nhất tháng này: đang được phân tích từ dữ liệu POS.",
    "Đơn hàng bị hủy hôm nay: 3 đơn. Lý do chủ yếu: hết hàng.",
    "Doanh thu tháng này tăng 12% so với cùng kỳ năm ngoái. Xuất sắc! 📈",
    "Báo cáo doanh thu theo ca đã sẵn sàng trong mục Báo cáo → Doanh thu.",
    "Khách hàng mới tháng này: 28 người. Khách hàng quay lại: 115 người.",
    "Tồn kho hiện tại: đang được cập nhật tự động sau mỗi giao dịch.",
    "Đơn hàng online chờ xử lý: 7 đơn. Vui lòng xử lý trong 2 giờ.",

    # ── Farm Management (8) ──────────────────────────────────────────────────
    "Báo cáo mùa vụ tháng này: 85% diện tích đã được chăm sóc đúng lịch.",
    "Lịch tưới nước khu A đã được cập nhật cho tuần tới.",
    "Phân bón đã được ghi nhận sử dụng: 50kg NPK cho khu B ngày hôm nay.",
    "Cảnh báo: Khu C có dấu hiệu sâu bệnh. Vui lòng kiểm tra và báo cáo.",
    "Thu hoạch dự kiến tuần tới: 2.5 tấn rau xanh, 800kg cà chua.",
    "Nhật ký nông trại ngày hôm nay đã được lưu thành công.",
    "Thiết bị tưới tự động khu D đang hoạt động bình thường. Độ ẩm đất: 68%.",
    "Lịch sử sản lượng 3 tháng qua đã được xuất báo cáo PDF.",

    # ── Customer Support Tickets (8) ─────────────────────────────────────────
    "Ticket #TKT-1042 của bạn đã được tiếp nhận. Thời gian xử lý dự kiến: 24 giờ.",
    "Ticket #TKT-1039 đã được đóng. Vấn đề đã được giải quyết thành công.",
    "Có 5 ticket đang chờ phản hồi từ phía bạn. Vui lòng kiểm tra.",
    "Đội hỗ trợ kỹ thuật sẽ liên hệ bạn trong vòng 2 giờ làm việc.",
    "Vấn đề thiết bị quét QR đã được ghi nhận và chuyển cho kỹ thuật viên.",
    "Phản hồi hài lòng của bạn đã được ghi nhận. Cảm ơn! ⭐⭐⭐⭐⭐",
    "Ticket ưu tiên cao #TKT-1055 đang được xử lý khẩn cấp.",
    "Báo cáo ticket tháng: 98% được giải quyết trong SLA. Rất tốt!",

    # ── Assets & Devices (7) ─────────────────────────────────────────────────
    "Laptop Dell XPS của bạn (tài sản #ASS-0023) đang được bảo hành đến tháng 8/2026.",
    "Yêu cầu cấp phát tài sản của bạn đã được gửi đến bộ phận IT.",
    "Thiết bị QR #QR-007 tại cổng chính vừa báo lỗi đọc thẻ. Đã ghi nhận sự cố.",
    "Kiểm kê tài sản quý 2 sẽ diễn ra từ ngày 01/06. Vui lòng chuẩn bị danh sách.",
    "Điện thoại công ty #PHN-012 đã được bàn giao thành công.",
    "Tài sản mà bạn đang sử dụng: 1 laptop, 1 màn hình phụ, 1 ghế ergonomic.",
    "Báo cáo khấu hao tài sản quý 1 đã được xuất cho bộ phận kế toán.",

    # ── Visitors (5) ─────────────────────────────────────────────────────────
    "Khách thăm #VIS-2026041801 đã check-in lúc 10:15. Đang gặp phòng Marketing.",
    "Có 3 khách đang chờ ở sảnh lễ tân. Vui lòng ra đón.",
    "Lượt khách tham quan hôm nay: 12 lượt. Cao hơn trung bình tuần 15%.",
    "Cuộc hẹn với khách hàng lúc 14:00 đã được xác nhận. Phòng họp B2 đã đặt sẵn.",
    "Khách VIP từ Hà Nội dự kiến đến vào 15:30. Vui lòng chuẩn bị tiếp đón.",

    # ── General Greetings & Small-talk (15) ──────────────────────────────────
    "Xin chào! Tôi là Thần Nông AI, trợ lý thông minh của iAttendance. Tôi có thể giúp gì cho bạn? 😊",
    "Chào buổi sáng! Hôm nay trời đẹp, chúc bạn có một ngày làm việc năng suất nhé! ☀️",
    "Tôi đang lắng nghe. Bạn cần hỗ trợ gì về hệ thống iAttendance?",
    "Câu hỏi hay đấy! Để tôi tra cứu thông tin cho bạn nhé.",
    "Tôi hiểu rồi. Dữ liệu của bạn đang được xử lý, vui lòng chờ trong giây lát.",
    "Rất vui được hỗ trợ bạn! Hệ thống iAttendance có đầy đủ các tính năng bạn cần.",
    "Chào buổi chiều! Bạn cần hỗ trợ gì không? Tôi luôn sẵn sàng giúp đỡ. 🤝",
    "Thông tin của bạn đã được ghi nhận thành công.",
    "Cảm ơn bạn đã sử dụng iAttendance! Nếu cần thêm hỗ trợ, hãy hỏi tôi bất cứ lúc nào.",
    "Tôi đã kiểm tra hệ thống. Mọi thứ đang hoạt động bình thường. ✅",
    "Xin lưu ý: Một số tính năng yêu cầu quyền truy cập cấp quản lý. Vui lòng liên hệ admin.",
    "Báo cáo của bạn đang được tạo. Tôi sẽ thông báo khi hoàn tất.",
    "Chúc mừng! Tháng này bạn đạt chuyên cần 100%. Công ty sẽ ghi nhận thành tích này. 🏆",
    "Hệ thống iAttendance vừa cập nhật phiên bản mới với nhiều tính năng cải tiến.",
    "Tôi đã chuyển yêu cầu của bạn đến phòng ban liên quan. Họ sẽ phản hồi sớm.",

    # ── Errors / Unknown Queries (10) ─────────────────────────────────────────
    "Xin lỗi, tôi chưa hiểu rõ yêu cầu của bạn. Bạn có thể diễn đạt lại không?",
    "Dữ liệu bạn cần hiện chưa có trong hệ thống. Vui lòng kiểm tra lại.",
    "Phiên làm việc của bạn đã hết hạn. Vui lòng đăng nhập lại để tiếp tục.",
    "Xin lỗi, tôi không có quyền truy cập thông tin này. Vui lòng liên hệ quản trị viên.",
    "Yêu cầu không hợp lệ. Vui lòng kiểm tra định dạng dữ liệu đầu vào.",
    "Hệ thống đang bảo trì. Vui lòng thử lại sau 15 phút. 🔧",
    "Câu hỏi của bạn nằm ngoài phạm vi hỗ trợ của tôi. Vui lòng liên hệ đội support.",
    "Không tìm thấy nhân viên với thông tin bạn cung cấp. Vui lòng kiểm tra lại mã nhân viên.",
    "Lỗi kết nối tạm thời. Hệ thống đã ghi nhận và đang xử lý. Vui lòng thử lại.",
    "Tôi xin lỗi vì sự bất tiện này. Vui lòng mô tả chi tiết hơn để tôi hỗ trợ tốt hơn.",
]

