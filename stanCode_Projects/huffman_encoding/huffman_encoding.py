"""
File: huffman_encoding.py
Name: Pei-Feng(Kevin) Ma
-----------------------------------
This program demonstrates the idea of zipping/unzipping
through the algorithm of Huffman Encoding.
We will be using all of the important concepts
we learned today to complete this hugh project.
"""

from ds import Tree, PriorityQueue

# The string to be zipped/unzipped
TARGET = 'stancode sc001 sc101'


def main():
    d = build_dict()

    ############################
    # TODO: Build a priority queue based on d
    priority_queue = PriorityQueue()
    for ch, count in d.items():
        tree = Tree(None, ch, None)
        priority_queue.enqueue((tree, count))
    #priority_queue.traversal()
    ############################
    tree = encoding(priority_queue)
    print(decoding(tree, '1010101101010100010100110100000101010101100111'))


def build_dict():
    """
    :return: dict, a Python dictionary containing ch as key,
                    the number of ch occurrence as value
    """
    dict = {}
    for ch in TARGET:
        if ch in dict:
            dict[ch]+=1
        else:
            dict[ch]=1
    return dict


def decoding(tree, unzip_words):
    """
    :param tree: Tree, the binary tree that contains all the ch encoded
    :param unzip_words: str, the mystery compressed binary digits to be unzipped
    :return: str, the unzipped words
    """
    current = tree
    ans= ''
    
    for ch in unzip_words:
        if ch == '0':
            current = current.left
        else: 
            current = current.right
        
        if current.left is None and current.right is None:
            ans += current.tree_value
            current = tree
    return ans


def encoding(pq):
    """
    :param pq: PriorityQueue, containing all the ch we need to encode
    :return: Tree, a binary tree that has all the ch encoded
    """

    while True:

        # dequeue and dequeue
        left = pq.dequeue()
        right = pq.dequeue()
        
        # build tree
        new_value = left.value[1]+right.value[1]
        tree = Tree(left.value[0], new_value, right.value[0])
        
        # finish
        if pq.length() == 0 :
            return tree
        
        # enqueue (continue)
        else:
            pq.enqueue((tree, new_value))





if __name__ == '__main__':
    main()
