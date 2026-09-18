class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


# Допоміжні функції для тестування (не частина алгоритму)
def build_list_with_cycle(values, pos):
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


if __name__ == "__main__":
    tests = [
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),
        ([1], -1),
    ]

    for values, pos in tests:
        head = build_list_with_cycle(values, pos)
        result = has_cycle(head)
        print(f"head = {values}, pos = {pos} -> {result}")
