import streamlit as st

# Tiêu đề ứng dụng
st.title("Ứng dụng Đếm Từ Trong Câu")

# Hướng dẫn người dùng
st.write("Nhập một câu vào ô bên dưới để đếm số lượng từ và tần suất xuất hiện của từng từ.")

# Nhập liệu từ người dùng
user_input = st.text_input("Nhập câu của bạn:")

# Khi người dùng nhập câu
if user_input:
    # Tách từ dựa trên khoảng trắng
    ds_tu = user_input.split()

    # Xử lý loại bỏ dấu câu và chuẩn hóa chữ thường
    ds_tu = [tu.strip(",.!?;:()[]\"'").lower() for tu in ds_tu]

    # Đếm số từ
    dem_tu = {}
    for tu in ds_tu:
        if tu:  # Bỏ qua từ rỗng
            dem_tu[tu] = dem_tu.get(tu, 0) + 1

    # Hiển thị kết quả
    st.subheader(f"Tổng số từ: {len(ds_tu)}")
    st.subheader("Tần suất từng từ:")
    st.write(dem_tu)
