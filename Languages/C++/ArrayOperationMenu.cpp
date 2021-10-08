#include <iostream>
using namespace std;

struct Array
{
    int *A;
    int size;
    int length;
};

void Display(struct Array a)
{
    int i;
    cout << "element are : ";
    for (i = 0; i < a.length; i++)
        cout << a.A[i]<<" ";
}

void Insert(struct Array *a, int index, int x)
{
    int i;
    if (index >= 0 && index <= a->size)
    {
        for (i = a->length; i > index; i--)
            a->A[i] = a->A[i - 1];

        a->A[index] = x;
        a->length++;
    }
    cout<<" Index : "<<index<<" And Element of Array : "<<a->A[index];
}

int Deletes(struct Array *a, int index)
{
    int x = 0;
    int i;
    if (index >= 0 && index < a->length)
    {
        x = a->A[index];
        for (i = index; i < a->length - 1; i++)
            a->A[i] = a->A[i + 1];
        a->length--;
        return x;
    }
    return 0;
}

void swap(int *a, int *b)
{
    int *temp = a;
    a = b;
    b = temp;
}

int LinearSearch(struct Array *a, int element)
{
    for (int i = 0; i < a->length; i++)
    {
        if (element == a->A[i])
        {
            swap(&a->A[i], &a->A[0]);
            return i;
        }
    }
    return -1;
}

int BinarySearch(struct Array *a, int element, int low, int high)
{
    int mid;
    while (low <= high)
    {
        mid = (low + high) / 2;
        if (element == a->A[mid])
            return mid;
        else if (element < a->A[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
    return -1;
}

int RBinSearch(struct Array *a, int element, int low, int high)
{
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (element == a->A[mid])
            return mid;
        else if (element < a->A[mid])

            RBinSearch(a, element, low, high = mid - 1);
        else
            RBinSearch(a, element, low = mid + 1, high);
    }
    return -1;
}


void Reverse(struct Array *a)
{
    int *b = new int[a->length];

    for (int i = a->length - 1, j = 0; i >= 0; i--, j++)
        b[j] = a->A[i];

    for (int i = 0; i < a->length; i++)
        a->A[i] = b[i];
    
    cout<<"Reverse of Array : ";
    for(int i=0;i<a->length;i++)
        cout<<a->A[i]<<" ";
}


void InsertSort(struct Array *a, int x)
{
    int i = a->length - 1;

    if (a->length == a->size)
        exit(0);

    while (i >= 0 && a->A[i] > x)
    {
        a->A[i + 1] = a->A[i];
        i--;
    }
    a->A[++i] = x;
    a->length++;
    cout<<"Added at Index : "<<i<<" And Element is : "<<a->A[i]<<endl;

}

bool sorted(struct Array *a)
{
    bool flag = true;
    for (int i = 0; i < a->length-1; i++)
    {
        if (a->A[i] > a->A[i + 1])
        {
            flag = false;
            break;
        }
    }
    return flag;
}

int main()
{
    struct Array ob;

    int ch;
    int low = 0,high;
    int element, index;
    cout << "Enter size : ";
    cin >> ob.size;
    ob.A = new int[ob.size];
    ob.length = 0;

    do
    {
        cout << "\n<-----*** Menu ***-----> \n";
        cout << "1. Insert \n";
        cout << "2. Sorted Insert \n";
        cout << "3. Delete \n";
        cout << "4. Array Reverse\n";
        cout << "5. Search \n";
        cout << "6. Display\n";
        cout << "7. Checking sorted Array\n";
        cout << "8. Exit  \n";

        cout << "Enter your choice : ";
        cin >> ch;

        switch (ch)
        {
        case 1:
            cout << "Enter index and element for insertion : ";
            cin >> index >> element;
            Insert(&ob, index, element);
            high = ob.length-1;
            break;
        case 2:
            cout << "Enter element for insertion : ";
            cin >>element;
            InsertSort(&ob,element);
            high = ob.length-1;
            break;

        case 3:
            cout << "Enter index for deletion : ";
            cin >> index;
            Deletes(&ob, index);
            break;
        
        case 4:
            Reverse(&ob);
            break;

        case 5:
            cout << "There are three search \n A. Linear search \n B. Binary search \n C. Binary search by Recursion \n";
            cout << "Enter your choice for required search : ";
            char chh;
            cin >> chh;
            switch (chh)
            {

            case 'A':
                cout << "Enter element for your required search : ";
                cin >> element;
                cout<<"Index at that element : "<<LinearSearch(&ob, element);
                break;
            case 'B':

                cout << "Enter element for your required search : ";
                cin >> element;
                cout<<"Index at that element : "<<BinarySearch(&ob, element, low, high);
                break;
            case 'C':

                cout << "Enter element for your required search : ";
                cin >> element;
                cout<<"Index at that element : "<<RBinSearch(&ob, element, low, high);
                break;
            }
            break;
        case 6:
            Display(ob);
            break;

        case 7:
            if(sorted(&ob))
               cout<<"\nArray is sorted\n";
            else 
               cout<<"\nArray is not sorted";
            break;

        case 8:
            cout << "exit";
            exit(0);
        }
    }while(ch<10);
    return (0);
}