class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 is not None else list2

    return dummy.next


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
        ([1, 2, 4], [1, 3, 4]),
        ([], []),
        ([], [0]),
    ]

    for l1_vals, l2_vals in tests:
        l1 = build_list(l1_vals)
        l2 = build_list(l2_vals)
        result = merge_two_lists(l1, l2)
        print(f"list1 = {l1_vals}, list2 = {l2_vals} -> {list_to_values(result)}")
