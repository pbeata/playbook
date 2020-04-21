#include <iostream>

using namespace std;

// stores the 3D coordinates of a node
// (if 2D, z will always be set to zero)
struct node
{
  int id;
  double x;
  double y;
  double z;
};


void print(node& N)
{
  cout << "Node is at: (" << N.x << ", " << N.y << ", " << N.z << ")\n";
}


int main()
{

  // we use structs to store a group of public/realted "data" 
  // without much complicated functionality
  
  node A;
  A.id = 42;
  A.x = 2.2;
  A.y = 4.1;
  A.z = 10.0;
  print(A);

  node B;
  B.id = 99;
  B.x = 2.0;
  B.y = 0.1;
  B.z = 1.0;
  print(B);

 	return 0;
}
