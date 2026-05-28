#include <iostream>
#include <random>

std::random_device rd;
std::mt19937 gen(rd());

int randomInt(int min, int max) {
    std::uniform_int_distribution<> dist(min, max);
    return dist(gen);
}

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
    friend std::ostream& operator<<(std::ostream& os, const ListNode& node);
};

std::ostream& operator<<(std::ostream& os, const ListNode& node) {
    os << node.val;
    return os;
}

void printLinkedList(ListNode* head) {
    std::cout << "[";
    while (head != nullptr) {
        std::cout << *head;
        if (head->next != nullptr) {std::cout << ", ";}
        head = head->next;
    }
    std::cout << "]";
}

ListNode* generateRandomAscendingLinkedList(int length, int minVal, int maxVal) {
    if (length == 0) { return nullptr; }
    int min = minVal;
    int max = maxVal;
    auto *head = new ListNode();

    ListNode *currentNode = head;
    for (int i = 0; i < length; ++i) {
        int randInt = randomInt(min, max);
        if (randInt > min) { min = randInt; }

        currentNode->val = randInt;

        if (i != length-1) {
            auto *newNode = new ListNode();
            currentNode->next = newNode;
            currentNode = newNode;
        }
    }
    return head;
}

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if ( (list1 == nullptr) and (list2 == nullptr) ) { return nullptr; }
        else if (list1 == nullptr) { return list2; }
        else if (list2 == nullptr) { return list1; }

        auto *head = new ListNode();

        ListNode *currentNode = head;
        while (list1 != nullptr) {
            if (list1->val <= list2->val) {
                currentNode->val = list1->val;

                if (list1->next == nullptr) {
                    currentNode->next = list2;
                    return head;
                }
                list1 = list1->next;

            } else if (list2->val < list1->val) {
                currentNode->val = list2->val;

                if (list2->next == nullptr) {
                    currentNode->next = list1;
                    return head;
                }
                list2 = list2->next;
            }

            auto newNode = new ListNode();
            currentNode->next = newNode;
            currentNode = newNode;
        }
        return head;
    }
};

int main() {
    Solution solve = Solution();
    ListNode *list1 = generateRandomAscendingLinkedList(20, -100, 100);
    ListNode *list2 = generateRandomAscendingLinkedList(10, -100, 100);
    ListNode *list3 = solve.mergeTwoLists(list1, list2);

    printLinkedList(list1);
    std::cout << std::endl;
    printLinkedList(list2);
    std::cout << std::endl;
    printLinkedList(list3);
    std::cout << std::endl;

    return 0;
}
