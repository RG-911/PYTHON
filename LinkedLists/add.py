from linked_list import LinkedList, Node, build_test_case

linked_list_a, linked_list_b = build_test_case()


def add_two(linked_list_a, linked_list_b):
    result = LinkedList()
    carry = 0
    node_a = linked_list_a.head
    node_b = linked_list_b.head
    while node_a or node_b:
        if node_a:
            node_a_val = node_a.val
            node_a = node_a.next
        else:
            node_a_val = 0

        if node_b:
            node_b_val = node_b.val
            node_b = node_b.next
        else:
            node_b_val = 0

        total = node_a_val + node_b_val
        if total > 9:
            carry = 1
            total %= 10
        else:
            carry = 0
        if not result.head:
            result.head = Node(total)
            temp = result.head
        else:
            temp.next = Node(total)
            temp = temp.next
    if carry:
        temp.next = Node(carry)
    return result


print("Adding linked list:\n{0}\nto linked list\n{1}\n".format(linked_list_a, linked_list_b))
result = add_two(linked_list_a, linked_list_b)
print("Result should be: 9 -> 5 -> 1 ->\nFunction returned:\n{0}".format(result))