import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cau hinh trang web
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="📚",
    layout="wide"
)

# 2. Tieu de
st.title("QUẢN LÝ ĐIỂM SINH VIÊN-")

# 3. Du lieu 10 sinh vien
data = {
    "Họ tên": [
        "Nguyễn Văn An",
        "Trần Thị Bình",
        "Lê Văn Cường",
        "Phạm Thị Dung",
        "Hoàng Văn Em",
        "Võ Thị Giang",
        "Đặng Văn Hùng",
        "Bùi Thị Lan",
        "Đỗ Văn Minh",
        "Nguyễn Thị Nga"
    ],
    "Chuyên cần": [9, 8, 7, 10, 6, 8, 9, 5, 7, 10],
    "Giữa kỳ": [8, 7, 6, 9, 5, 8, 7, 4, 6, 9],
    "Cuối kỳ": [9, 8, 7, 9, 4, 9, 8, 5, 6, 10]
}

df = pd.DataFrame(data)

# 4. Tinh diem tong ket
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
)

# 5. Xep loai
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# 6. Bang diem
st.header("1. Bảng điểm 10 sinh viên")

st.dataframe(
    df.style.format({"Tổng kết": "{:.2f}"}),
    use_container_width=True,
    hide_index=True
)

# 7. Thong ke
st.header("2. Thống kê kết quả học tập")

diem_tb = df["Tổng kết"].mean()
diem_max = df["Tổng kết"].max()
diem_min = df["Tổng kết"].min()
so_sv_dat = int((df["Tổng kết"] >= 5).sum())

sv_max = df[df["Tổng kết"] == diem_max]
sv_min = df[df["Tổng kết"] == diem_min]

cot1, cot2, cot3 = st.columns(3)

cot1.metric("Điểm trung bình lớp", f"{diem_tb:.2f}")
cot2.metric("Số sinh viên đạt", f"{so_sv_dat}/10")
cot3.metric("Số sinh viên", len(df))

st.subheader("Sinh viên có điểm tổng kết cao nhất")
st.write(f"Điểm cao nhất: {diem_max:.2f}")
st.write(", ".join(sv_max["Họ tên"].tolist()))

st.subheader("Sinh viên có điểm tổng kết thấp nhất")
st.write(f"Điểm thấp nhất: {diem_min:.2f}")
st.write(", ".join(sv_min["Họ tên"].tolist()))

# 8. Selectbox va thong tin sinh vien
st.header("3. Tra cứu sinh viên")

ten_chon = st.selectbox(
    "Chọn họ tên sinh viên:",
    df["Họ tên"].tolist()
)

sv = df[df["Họ tên"] == ten_chon].iloc[0]

st.subheader(f"Thông tin sinh viên: {ten_chon}")

c1, c2, c3 = st.columns(3)

c1.metric("Chuyên cần", f"{sv['Chuyên cần']:.2f}")
c1.metric("Giữa kỳ", f"{sv['Giữa kỳ']:.2f}")

c2.metric("Cuối kỳ", f"{sv['Cuối kỳ']:.2f}")
c2.metric("Tổng kết", f"{sv['Tổng kết']:.2f}")

c3.metric("Xếp loại", sv["Xếp loại"])

# 9. Bieu do cot
st.header("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(df["Họ tên"], df["Tổng kết"])

ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

# 10. Thong tin nguoi tao
st.divider()

st.markdown(
    """
    <div style="text-align:center; color:gray; font-size:12px;">
        Người tạo: ĐẶNG HƯƠNG TRẦM<br>
        MSSV: 052208006213
    </div>
    """,
    unsafe_allow_html=True
)
