#include <iostream>

using namespace std;

template <class T>
class Node
{
private:
	Node *prev;
	T value;
	Node *next;

public:
	Node(Node *inPrev, const T inVal, Node *inNext)
	{
		prev = inPrev;
		value = inVal;
		next = inNext;
		cout << "create node value = " << value << endl;
	}
	~Node()
	{
		cout << "destroy node value = " << value << endl;
	}
	void setPrevAndNext()
	{
		if (prev != NULL)  prev->next = this;
		if (next != NULL)  next->prev = this;
	}
	void printValue()
	{
		cout << " (" << value << ") ";
	}
	T getValue()
	{
		return value;
	}
	Node* getNext()
	{
		return next;
	}
	Node* getPrev()
	{
		return prev;
	}
	void setPrevToNull()
	{
		prev = NULL;
	}
	void setNextToNull()
	{
		next = NULL;
	}
};


/* Functions:

clear
size
isEmpty

add (to tail by default)
addFirst (to head)
addLast (to tail, called by add by default)

peekFirst (check first element)
peekLast 

removeFirst (remove the head)
removeLast

remove (remove an arbitrary node)
removeAtIndex
remove(object) and support NULL values

indexOf(object)
bool contains

*/

template <class T>
class List
{
private:
	Node<T> *head;
	Node<T> *tail;
	int size;

public:
	List()
	{
		size = 0;
		head = NULL;
		tail = NULL;
	}
	~List()
	{
		clearList();
	}

	int getSize()
	{
		return size;
	}

	void clear()
	{
		if (size == 0)
		{
			cout << "list is already empty!" << endl;
		}		
		else
		{
			Node<T> *temp = head;
			
		}
	}

	void clearList()
	{
		if (size == 0)
		{
			cout << "list is already empty!" << endl;
		}
		else
		{
			bool emptyList = false;
			Node<T> *temp = head;
			while (!emptyList)
			{
				if (head != tail)
				{
					head = temp->getNext();
					head->setPrevToNull();
					temp->setPrevToNull();
					temp->setNextToNull();
					delete(temp);
					size--;
					temp = head;
				}
				else
				{
					delete(temp);
					size--;
					emptyList = true;
				}
			}
			head = NULL;
			tail = NULL;
			cout << "check size one last time: " << size << endl;
		}
	}

	void insertFirstNode(const T& inVal)
	{
		Node<T> *newNode = new Node<T> (NULL, inVal, NULL);
		head = newNode;
		tail = newNode;
		size++;
	}
	void addNodeToBack(const T& inVal)
	{
		if (size == 0)
		{
			insertFirstNode(inVal);
		}
		else
		{
			Node<T> *temp = tail;
			Node<T> *newNode = new Node<T> (temp, inVal, NULL);
			newNode->setPrevAndNext();
			tail = newNode;
			size++;
		}
	}
	void addNodeToFront(const T& inVal)
	{
		if (size == 0)
		{
			insertFirstNode(inVal);
		}
		else
		{
			Node<T> *temp = head;
			Node<T> *newNode = new Node<T> (NULL, inVal, temp);
			newNode->setPrevAndNext();
			head = newNode;
			size++;
		}
	}
	bool findVal(const T& inVal)
	{
		if (size == 0)
		{
			cout << "LIST IS EMPTY! NOTHING TO SEARCH\n";	
			return false;
		}
		else
		{
			Node<T> *iter = head;
			T temp;

			while (iter != NULL)
			{
				temp = iter->getValue();
				if (temp == inVal)
				{
					return true;
				}
				iter = iter->getNext();
			}

			// If we traverse the whole list and don't find
			// a match, then return false
			return false;
		}
	}

	void removeFirst()
	{
		if (size == 0)  
		{
			cout << "LIST IS EMPTY! NOTHING TO REMOVE\n";
		}
		else
		{
			Node<T> *temp = head;
			head = temp->getNext();
			temp->setNextToNull();
			if (head != NULL) head->setPrevToNull();

			T tempVal = temp->getValue();
			delete(temp);
			size--;

			cout << "NEW LIST: removed head = " << tempVal << endl;
			this->print();
		}
	}
	void removeLast()
	{
		if (size == 0)  
		{
			cout << "LIST IS EMPTY! NOTHING TO REMOVE\n";
		}
		else
		{
			Node<T> *temp = tail;
			tail = temp->getPrev();
			temp->setPrevToNull();
			if (tail != NULL) tail->setNextToNull();

			T tempVal = temp->getValue();
			delete(temp);
			size--;

			cout << "NEW LIST: removed head = " << tempVal << endl;
			this->print();
		}
	}

	void print()
	{
		if (size == 0)  
		{
			cout << "LIST IS EMPTY! NOTHING TO PRINT\n";
		}
		else
		{
			cout << "\nsize of the list = " << size << endl;

			cout << "[START] ";
			Node<T> *iter = head;
			while (iter != NULL)
			{
				iter->printValue();	
				iter = iter->getNext();
			}
			cout << " [END]\n" << endl;
		}
	}
};



int main()
{

	List<int> riderID;
	riderID.addNodeToBack(5);
	riderID.addNodeToBack(23);
	riderID.addNodeToBack(7);
	riderID.addNodeToBack(13);

	// search for a value
	bool valueExists;
	valueExists = riderID.findVal(7);
	cout << valueExists << endl;
	valueExists = riderID.findVal(22);
	cout << valueExists << endl;
	riderID.print();


	riderID.removeFirst();
	riderID.removeLast();
	riderID.removeFirst();
	riderID.removeLast();

	List<float> riderCash;
	riderCash.addNodeToFront(13.0f);
	riderCash.addNodeToFront(7.0f);
	riderCash.addNodeToFront(23.0f);
	riderCash.addNodeToFront(5.0f);
	
	valueExists = riderCash.findVal(7.0f);
	cout << valueExists << endl;
	valueExists = riderCash.findVal(22.0f);
	cout << valueExists << endl;
	riderCash.print();

	return 0;
}
