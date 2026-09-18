class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head):
    current = head

    while current is not None and current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


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


if __name__ == "__main__":
    tests = [
        [1, 1, 2],
        [1, 1, 2, 3, 3],
    ]

    for values in tests:
        head = build_list(values)
        result = delete_duplicates(head)
        print(f"head = {values} -> {list_to_values(result)}")
