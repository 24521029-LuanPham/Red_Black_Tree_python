# ==============================================================================
# File: red_black_tree.py
# Mô tả: Định nghĩa cấu trúc Node và các thao tác cốt lõi của Cây Đỏ Đen (Red-Black Tree).
# Bao gồm các thao tác: Thêm node, cân bằng cây (xoay, đổi màu), tìm kiếm và in cây.
# ==============================================================================

class Node:
    """
    Lớp đại diện cho một nút (node) trong Cây Đỏ Đen.
    """
    def __init__(self, data):
        self.data = data            # Giá trị khóa của nút
        self.parent = None          # Con trỏ trỏ đến nút cha
        self.left = None            # Con trỏ trỏ đến con trái
        self.right = None           # Con trỏ trỏ đến con phải
        self.color = "RED"          # Mặc định nút mới thêm vào sẽ có màu Đỏ

class RedBlackTree:
    """
    Lớp quản lý Cây Đỏ Đen với các quy tắc cân bằng chặt chẽ.
    """
    def __init__(self):
        # Khởi tạo nút TNULL (Nút rỗng/Sentinel node)
        # Trong Cây Đỏ Đen, các nút lá trỏ vào một nút TNULL có màu Đen.
        self.TNULL = Node(0)
        self.TNULL.color = "BLACK"
        self.root = self.TNULL

    def create_tree(self, keys):
        """
        Tạo cây từ một danh sách các khóa.
        :param keys: Danh sách (list) các số nguyên.
        """
        for key in keys:
            self.insert(key)

    def search(self, k):
        """
        Tìm kiếm một khóa trong cây.
        :param k: Khóa cần tìm.
        :return: Nút chứa khóa nếu tìm thấy, ngược lại trả về nút TNULL.
        """
        return self._search_tree_helper(self.root, k)

    def _search_tree_helper(self, node, key):
        # Nút hiện tại là TNULL hoặc tìm thấy khóa
        if node == self.TNULL or key == node.data:
            return node
        # Nếu khóa cần tìm nhỏ hơn khóa hiện tại, rẽ trái
        if key < node.data:
            return self._search_tree_helper(node.left, key)
        # Nếu khóa cần tìm lớn hơn khóa hiện tại, rẽ phải
        return self._search_tree_helper(node.right, key)

    def insert(self, key):
        """
        Thêm một khóa mới vào cây và tiến hành cân bằng lại cây.
        :param key: Giá trị số nguyên cần thêm.
        """
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "RED" # Nút mới luôn là màu Đỏ theo quy tắc Cây Đỏ Đen

        y = None
        x = self.root

        # Bước 1: Tìm vị trí để chèn nút mới
        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None: # Cây đang rỗng, nút mới chính là gốc
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        # Nếu nút mới là gốc, chuyển thành Đen và kết thúc
        if node.parent is None:
            node.color = "BLACK"
            return

        # Nếu ông nội không tồn tại, chưa cần cân bằng
        if node.parent.parent is None:
            return

        # Bước 2: Gọi hàm sửa lỗi để đảm bảo các quy tắc của Cây Đỏ Đen được giữ vững
        self._fix_insert(node)

    def _fix_insert(self, k):
        """
        Hàm cốt lõi để cân bằng lại cây sau khi chèn.
        Xử lý trường hợp "Xung đột đỏ-đỏ" (Nút hiện tại màu Đỏ và Nút cha cũng màu Đỏ).
        """
        while k.parent.color == "RED":
            # Trường hợp 1: Nút cha là con trái của nút ông nội
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right # u là "nút chú" (uncle) của k
                
                # Trường hợp 1.1: Nút chú u có màu Đỏ -> Đổi màu cha, chú và ông nội
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent # Đẩy vấn đề lên nút ông nội để tiếp tục kiểm tra
                else:
                    # Trường hợp 1.2: Nút chú u có màu Đen và k là con phải -> Xoay trái
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    # Trường hợp 1.3: Nút chú u có màu Đen và k là con trái -> Xoay phải và đổi màu
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._right_rotate(k.parent.parent)
            
            # Trường hợp 2: Nút cha là con phải của nút ông nội (Đối xứng với Trường hợp 1)
            else:
                u = k.parent.parent.left # u là "nút chú"
                
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._left_rotate(k.parent.parent)
            
            # Đảm bảo vòng lặp không bị lỗi nếu k bị đẩy lên tới root
            if k == self.root:
                break
                
        # Quy tắc tối thượng: Nút gốc luôn luôn phải là màu Đen
        self.root.color = "BLACK"

    def _left_rotate(self, x):
        """ Xoay trái tại nút x """
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        """ Xoay phải tại nút x """
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def print_tree_directory(self):
        """
        In cây ra console dưới dạng cấu trúc thư mục phân cấp, 
        """
        if self.root == self.TNULL:
            print("Cây hiện đang rỗng.")
            return
        # Bắt đầu in từ nút gốc với nhãn [ROOT]
        self._print_helper(self.root, "", True, "[ROOT]")

    def _print_helper(self, node, indent, is_last, position):
        """ 
        Hàm đệ quy hỗ trợ in cây có thêm tham số 'position' để biết là Trái hay Phải 
        """
        if node != self.TNULL:
            print(indent, end="")
            if is_last:
                print("\\--", end="")
                indent += "    "
            else:
                print("|--", end="")
                indent += "|   "

            # Lấy ký tự màu (R cho Red, B cho Black)
            color_char = "R" if node.color == "RED" else "B"
            
            # In ra vị trí (Gốc/Trái/Phải) + Màu sắc + Giá trị
            print(f"{position} ({color_char}) {node.data}")

            # Đệ quy in con trái (luôn trỏ [T]) và con phải (luôn trỏ [P])
            self._print_helper(node.left, indent, False, "[T]")
            self._print_helper(node.right, indent, True, "[P]")