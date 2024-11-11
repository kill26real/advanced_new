"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход путь до файла с логами
    и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, хранящиеся в бинарном дереве уникальны
"""
import itertools
import logging
import random
from collections import deque
from dataclasses import dataclass
from typing import Optional
import re

logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(1, 10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)
    node_right = get_tree(max_depth - 1, level=level + 1)
    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass


def restore_tree(path_to_log_file: str) -> Optional[BinaryTreeNode]:
    visit_pattern = re.compile(r"Visiting <BinaryTreeNode\[(\d+)]>")
    left_add_pattern = re.compile(r"<BinaryTreeNode\[(\d+)]> left is not empty. Adding <BinaryTreeNode\[(\d+)]>")
    right_add_pattern = re.compile(r"<BinaryTreeNode\[(\d+)]> right is not empty. Adding <BinaryTreeNode\[(\d+)]>")

    nodes = {}
    root = None
    queue = deque()

    with open(path_to_log_file, "r") as log_file:
        for line in log_file:
            visit_match = visit_pattern.search(line)

            if visit_match:
                node_val = int(visit_match.group(1))
                if node_val not in nodes:
                    nodes[node_val] = BinaryTreeNode(node_val)
                current_node = nodes[node_val]

                if root is None:
                    root = current_node

                queue.append(current_node)
                continue

            left_add_match = left_add_pattern.search(line)
            if left_add_match:
                parent = int(left_add_match.group(1))
                left_child = int(left_add_match.group(2))

                if left_child not in nodes:
                    nodes[left_child] = BinaryTreeNode(left_child)
                nodes[parent].left = nodes[left_child]
                continue

            right_add_match = right_add_pattern.search(line)
            if right_add_match:
                parent = int(right_add_match.group(1))
                rigth_child = int(right_add_match.group(2))

                if rigth_child not in nodes:
                    nodes[rigth_child] = BinaryTreeNode(rigth_child)
                nodes[parent].right = nodes[rigth_child]
                continue

    return root


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename="walk_log_4.txt",
    )

    root = get_tree(7)
    walk(root)
