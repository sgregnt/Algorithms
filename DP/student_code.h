//you can include standard C++ libraries here

//required libraries
#include <vector>
#define MAX_N 30
#define CMB 8
#define BIT_L 3

// This function should return your name.
// The name should match your name in Canvas
//
void GetStudentName(std::string& your_name)
{
   your_name.assign("Gregory Naisat");
}

// Initialize matrix M, that stores OPT values. 
//
// w - vector of weights. 
// N - number of elements in w. 
void init_3bits_array(int(*array)[MAX_N][CMB], int *w, int N)
{
	int bit = 3;
	int lim;

	// M[0,...,n][7] = -1 are illegal value.
	for (int i = 0; i < N + 1; ++i) {
		(*array)[i][CMB - 1] = -1;
	}

	// all strings less than 2 have should include all characters:
	(N > bit - 1) ? (lim = bit - 1) : (lim = N);

	for (int i = 0; i < lim; ++i) {
		for (int j = 0; j < CMB - 1; ++j) {
			(*array)[i][j] = w[0] + w[1];
		}
	}
	// M[4][abcd] = aw1 + bw2 + cw3 + dw4
	//
	for (int i = 0; i < CMB - 1; ++i) {
		(*array)[bit - 1][i] = w[0] * (i & 1) + w[1] * (i >> 1 & 1) + w[2] * (i >> 2 & 1);
	}
}

// Update matrix at "M[step][bcd]" position.
//
// w array of weights.
// N number of elements in w.
void update_3bit_step(int(*array)[MAX_N][CMB], int *w, int step, int bcd, int N)
{
	int cd0;    // prev. combination asuming 0 bit.
	int cd1;    // prev. combination asuming 1 bit.
	int cd0_val; // optimal value for step - 1 for cd0
	int cd1_val; // optimal value for step - 1 for cd1
	int b; // MS-bit of the word bcd.

   // if bcd = CMB-1 (111), this is not spares and so 
   // we put -1.
   //
	if (bcd == CMB - 1) {
		(*array)[step][bcd] = -1;
	}
	else {

		//last bit 
		//
		b = ((bcd >> 2) & 1);

		cd0 = ((bcd << 1) & 6);
		cd1 = ((bcd << 1) & 6) + 1;

		// retrieve optimal values for possible previous combinations
		//
		cd0_val = (*array)[step - 1][cd0];
		cd1_val = (*array)[step - 1][cd1];

		if (cd1_val == -1) {
			// not a spare combination 
			(*array)[step][bcd] = cd0_val + w[step] * b;			
		}
		else {
			if (cd0_val > cd1_val) {
				(*array)[step][bcd] = cd0_val + w[step] * b;
			}
			else{
				(*array)[step][bcd] = cd1_val + w[step] * b;				
			}
		}
	}
}

int FindMaximumProfit(std::vector<int> w)
{
	int M[MAX_N][CMB] = { 0 }; // stores optimal values 
	int v[MAX_N] = { 0 }; // inner representation of w
	int res; // optimal value
    
    // number of elements in w
	int N = static_cast<int>(w.size());

	std::copy(w.begin(), w.end(), v);
	init_3bits_array(&M, v, N);
    
    // populate matrix M with optimal values.
    //
	for (int step = BIT_L; step < N; ++step) {
		for (int i = 0; i < CMB; ++i) {
			update_3bit_step(&M, v, step, i, N);
		}
	}
    
    // retrieve the maximum value
    //
	res = 0;
	for (int i = 0; i < CMB; ++i) {
		if (M[N - 1][i] > res) {
			res = M[N - 1][i];
		}
	}
	return res;
}

