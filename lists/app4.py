class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head):
    if head is None or head.next is None:
        return head

    slow, fast = head, head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    second_half = slow.next
    slow.next = None

    prev = None
    current = second_half
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    second_half = prev

    first_half = head
    while second_half is not None:
        first_tmp = first_half.next
        second_tmp = second_half.next

        first_half.next = second_half
        second_half.next = first_tmp

        first_half = first_tmp
        second_half = second_tmp

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
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
    ]

    for values in tests:
        head = build_list(values)
        reorder_list(head)
        print(f"head = {values} -> {list_to_values(head)}")
