# ==============================================================================
# File: main.py
# Mô tả: Chương trình chính cung cấp giao diện Console (CLI) để người dùng 
# tương tác với cấu trúc dữ liệu Cây Đỏ Đen.
# ==============================================================================

import sys
# Import lớp RedBlackTree từ file red_black_tree.py cùng thư mục
from red_black_tree import RedBlackTree

def display_menu():
    """
    Hàm in ra màn hình các lựa chọn của chương trình.
    """
    print("\n" + "="*45)
    print("   CHƯƠNG TRÌNH QUẢN LÝ CÂY ĐỎ ĐEN")
    print("="*45)
    print("1. Tạo cây từ tập khóa (Nhập mảng)")
    print("2. In cây (Theo định dạng cây thư mục)")
    print("3. Thêm một khóa mới vào cây")
    print("4. Tìm khóa trên cây")
    print("0. Thoát chương trình")
    print("="*45)

def main():
    """
    Hàm điều khiển luồng chính của chương trình.
    """
    # Khởi tạo một đối tượng Cây Đỏ Đen rỗng
    rb_tree = RedBlackTree()
    
    while True:
        display_menu()
        choice = input("Vui lòng nhập lựa chọn của bạn (0-4): ").strip()
        
        if choice == '1':
            try:
                # Nhận chuỗi đầu vào, cắt bằng khoảng trắng và ép kiểu sang số nguyên
                input_str = input(">> Nhập các khóa cách nhau bởi khoảng trắng (VD: 10 20 5): ")
                keys_list = [int(x) for x in input_str.split()]
                
                # Gọi hàm tạo cây
                rb_tree.create_tree(keys_list)
                print(f"[THÀNH CÔNG] Đã tạo cây với các khóa: {keys_list}")
            except ValueError:
                print("[LỖI] Vui lòng chỉ nhập các chữ số nguyên, cách nhau bởi khoảng trắng!")
                
        elif choice == '2':
            print("\n>> Cấu trúc Cây Đỏ Đen hiện tại:")
            rb_tree.print_tree_directory()
            
        elif choice == '3':
            try:
                key_to_insert = int(input(">> Nhập khóa (số nguyên) cần thêm: "))
                rb_tree.insert(key_to_insert)
                print(f"[THÀNH CÔNG] Đã thêm khóa {key_to_insert} vào cây!")
            except ValueError:
                print("[LỖI] Khóa nhập vào phải là một số nguyên!")
                
        elif choice == '4':
            try:
                key_to_search = int(input(">> Nhập khóa cần tìm: "))
                result_node = rb_tree.search(key_to_search)
                
                # Kiểm tra xem kết quả trả về có phải là nút TNULL (rỗng) hay không
                if result_node != rb_tree.TNULL:
                    print(f"[KẾT QUẢ] Khóa {key_to_search} TỒN TẠI trong cây (Màu: {result_node.color}).")
                else:
                    print(f"[KẾT QUẢ] Khóa {key_to_search} KHÔNG TỒN TẠI trong cây.")
            except ValueError:
                print("[LỖI] Khóa nhập vào phải là một số nguyên!")
                
        elif choice == '0':
            print("\n>> Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            sys.exit() # Kết thúc chương trình an toàn
            
        else:
            print("[LỖI] Lựa chọn không hợp lệ. Vui lòng nhập số từ 0 đến 4.")

# Điểm bắt đầu thực thi chương trình
if __name__ == "__main__":
    main()