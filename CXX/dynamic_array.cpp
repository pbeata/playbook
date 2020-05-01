#include <iostream>

using namespace std;

class dynamic_array
{

public:
	dynamic_array()
	{
		capacity = default_capacity;
		array = new int[capacity];
		length = 0;  // because the user didn't specify a size
		cout << "created dynamic_array object\n";
	}
	dynamic_array(int custom_capacity)
	{
		if (custom_capacity < 1)
		{
			cout << "***WARNING: capacity must be greater than or equal to 1\n";
			cout << "(setting to default of " << default_capacity << " instead)\n";
			capacity = default_capacity;
			length = 0;
		}
		else
		{
			capacity = custom_capacity;
			length = capacity;
		}
		array = new int[capacity];
		cout << "created dynamic_array object\n";
	}
	~dynamic_array()
	{
		delete[] array;
		cout << "destroyed dynamic_array object\n";
	}

	int size() { return length; }
	bool is_empty() { return size() == 0; }
	
	int get(int index) {
		if ( (index >= 0) && (index < length) )  return array[index];
		else  return -1;
	}

	void set(int index, int value) {
		if ( (index >= 0) && (index < length) )  array[index] = value;
		else  cout << "***ERROR: index not in range of array\n";
	}

	void clear() {
		for (int i = 0; i < capacity; i++)  array[i] = 0;
		length = 0;
	}

	// add a value to the end of the array
	void add(int value) {
		if (length >= capacity)
		{
			cout << "*resizing array!\n"; 

			// copy current values to a temporary array
			int *old = new int[capacity];
			for (int i = 0; i < length; ++i)
			{
				// old[i] = this->get(i);
				old[i] = array[i];
			}
			delete[] array;

			// resize the array
			capacity = 2 * capacity;
			array = new int[capacity];
			for (int i = 0; i < length; ++i)
			{
				array[i] = old[i];
			}
			delete[] old;
		}
		array[length] = value;
		length++;
	}

	// TODO:
	// void remove_at(int index);
	// bool remove_value(int value);  // use binary search to see if it exists
	// int find_index(int value);
	// int contains(int value);



private:
	int *array;
	int length;
	int capacity;	
	const int default_capacity = 16;
};

int main()
{
	const int n = 10;
	int m;

	dynamic_array A;
	dynamic_array B(n);
	dynamic_array C(-2);

	cout << A.size() << "  " << B.size() << "  " << C.size() << endl;
	cout << A.is_empty() << "  " << B.is_empty() << "  " << C.is_empty() << endl;

	for (int i = 0; i < n; i++) {
		B.set(i, i*i);
	}

	// do some work on the array...

	for (int i = 0; i < n; i++)
	{
		cout << i << " " << B.get(i) << endl;
	}

	for (int i = 0; i < 2*n; ++i)
	{
		B.add(100);
		m = B.size();
		cout << m << " " << B.get(m-1) << endl;
	}

	return 0;
}