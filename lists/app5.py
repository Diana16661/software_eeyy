class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next


# Допоміжні функції для тестування (не частина алгоритму)
def build_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def list_to_values(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


def find_node(head, value):
    current = head
    while current is not None:
        if current.val == value:
            return current
        current = current.next
    return None


if __name__ == "__main__":
    tests = [
        ([4, 5, 1, 9], 5),
        ([4, 5, 1, 9], 1),
    ]

    for values, target_val in tests:
        head = build_list(values)
        node = find_node(head, target_val)
        delete_node(node)
        print(f"head = {values}, node = {target_val} -> {list_to_values(head)}")
