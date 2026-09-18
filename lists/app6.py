class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def _reverse(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def double_number(head):
    reversed_head = _reverse(head)

    carry = 0
    current = reversed_head
    last = None
    while current is not None:
        total = current.val * 2 + carry
        current.val = total % 10
        carry = total // 10
        last = current
        current = current.next

    if carry:
        last.next = ListNode(carry)

    return _reverse(reversed_head)


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
        [1, 8, 9],
        [9, 9, 9],
    ]

    for values in tests:
        head = build_list(values)
        result = double_number(head)
        print(f"head = {values} -> {list_to_values(result)}")
