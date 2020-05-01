//required libraries
#include <string>

//you can include standard C++ libraries here



// This function should return your name.
// The name should match your name in Canvas
#define MAX_N 2000
#define MAX_C 4001
#define NINF -200000

int GetLeafs(int N)
{
	if ((N - 1) % 2 == 0) {
		return ((N - 1) - 2) / 2 + 1;
	}
	else {
		return ((N - 1) - 1) / 2 + 1;
	}
}
int GetParetIndex(int c)
{
	if (c % 2 == 0) {
		return (c - 2) / 2;
	}
	else
	{
		return (c - 1) / 2;
	}
}

int* GetChildren(int p, int N)
{
	int c[2];
	c[0] = -1;
	c[1] = -1;

	if ((2 * p + 2) < N) {
		c[0] = 2 * p + 1;
		c[1] = 2 * p + 2;
	}
	else
	{
		if ((2 * p + 1) < N) {
			c[0] = 2 * p + 1;
			c[1] = -1;
		}
	}
	return c;
}

int initT(int T[MAX_N][2][MAX_C], int* v, int child_start, int N, int nn_max, int cc_max) {
	for (int i = 0; i < nn_max; ++i) {
		for (int j = 0; j < cc_max; ++j) {
			T[i][0][j] = NINF;
			T[i][1][j] = NINF;
		}
	}

	for (int i = child_start; i < N; ++i) {

		for (int j = 0; j < cc_max; ++j) {
			T[i][0][j] = NINF;
			T[i][1][j] = NINF;
		}

		// if leaf is not connected cannot upstream charge.
		//
		T[i][0][0] = v[i] * v[i];

		// if leaf is connected then it upstreams all its charge. 
		//
		// offset to the center
		//
		T[i][1][nn_max + v[i]] = 0;
	}
	return 0;
}

int max_val(int* ar, int L) {
	int temp = NINF;
	for (int i = 0; i < L; i++)
	{
		if (ar[i] > temp)
			temp = ar[i];
	}
	return temp;
}


int max_val_2d(int ar[MAX_C][MAX_C], int L1, int L2) {
	int temp = NINF;
	for (int i = 0; i < L1; i++) {
		for (int j = 0; j < L2; j++)
		{
			if (ar[i][j] > temp)
				temp = ar[i][j];
		}
	}
	return temp;
}

int T_v_zero_zero(int N, int parent_start, int T[MAX_N][2][MAX_C], int v[MAX_N], int nn_max, int cc_max, int max_charge) {

	int a, b, c, e, f, p, p_l, p_r, r;
	int tmp1, tmp2, tmp3, tmp4;
	int* pc;
	int aux_list[MAX_C];
	int aux_list2[4];
	int aux_list_2d[MAX_C][MAX_C];
	int max_a = NINF;

	p = parent_start;
	pc = GetChildren(p, N);

	p_l = pc[0];
	p_r = pc[1];

	tmp1 = T[p_l][0][0] + T[p_r][0][0] + v[p] * v[p];
	max_a = tmp1;

	// include left child only
	//
	for (int i = nn_max - max_charge; i < nn_max + max_charge; ++i) {
		a = T[p_l][1][i];
		b = T[p_r][0][0];

		// offset back to -MAX_N, 0, MAX_N range
		//
		e = (v[p] + (i - nn_max));
		r = a + b + (e) * (e);
		if (r > max_a) {
			max_a = r;
		}
	}
	tmp2 = max_val(aux_list, cc_max);

	// include right child only
	//
	for (int i = nn_max - max_charge; i < nn_max + max_charge; ++i) {
		a = T[p_l][0][0];
		b = T[p_r][1][i];

		// offset back to -MAX_N, 0, MAX_N range
		//
		e = (v[p] + (i - nn_max));
		r = a + b + (e) * (e);
		if (r > max_a) {
			max_a = r;
		}
	}

	// include both children only
	//	
	for (int i = nn_max - max_charge; i < nn_max + max_charge; ++i) {
		for (int j = nn_max - max_charge; j < nn_max + max_charge; ++j) {
			a = T[p_l][1][j];
			b = T[p_r][1][i];

			// offset back to -MAX_N, 0, MAX_N range
			//
			e = (v[p] + (i - nn_max) + (j - nn_max));
			r = a + b + (e) * (e);
			if (r > max_a) {
				max_a = r;
			}
		}
	}

	a = max_a;
	return a;
}

int T_v_one_upstream(int N, int upstream, int parent_start, int T[MAX_N][2][MAX_C], int v[MAX_N], int nn_max, int cc_max, int max_charge) {

	int a, b, c, e, f, p, p_l, p_r, r;
	int tmp1, tmp2, tmp3, tmp4;
	int* pc;
	int aux_list[MAX_C];
	int aux_list2[4];
	int aux_list_2d[MAX_C][MAX_C];
	int max_a = NINF;

	p = parent_start;
	pc = GetChildren(p, N);

	p_l = pc[0];
	p_r = pc[1];

	// current charge is exactly the upstream charge.
	//
	if ((upstream - nn_max) == v[p]) {
		tmp1 = T[p_l][0][0] + T[p_r][0][0];
	}
	else {
		tmp1 = NINF;
	}

	max_a = tmp1;

	// include left child 
	//
	for (int i = nn_max - max_charge; i < nn_max + max_charge; ++i) {

		// Offset upstream
		//
		if ((upstream - nn_max) == (i - nn_max) + v[p]) {
			a = T[p_l][1][i];
			b = T[p_r][0][0];

			// Offset upstream 
			//
			//e = (v[p] + (i- MAX_N));
			//r = a + b + (e) * (e);

			// current charge is upstreamed
			r = b + a;
		}
		else
		{
			r = NINF;
		}
		if (r > max_a) {
			max_a = r;
		}
	}
	tmp2 = max_a;

	// include right child 
	//
	for (int i = nn_max - max_charge; i < nn_max + max_charge; ++i) {

		// Offset upstream
		//
		if ((upstream - nn_max) == (i - nn_max) + v[p]) {
			a = T[p_l][0][0];
			b = T[p_r][1][i];

			// current charge is upstreamed
			//
			r = a + b;
		}
		else
		{
			r = NINF;
		}
		if (r > max_a) {
			max_a = r;
		}
	}
	tmp3 = max_a;

	// include both children
	//	
	for (int i = nn_max - max_charge; i < nn_max + max_charge; ++i) {
		for (int j = nn_max - max_charge; j < nn_max + max_charge; ++j) {


			if ((p == 2)&(upstream == 23)) {
				a = 5;
				if ((i == 21) & (j == 21))
				{
					a = 5;
				}
			}

			// Offset upstream 
			//
			if ((upstream - nn_max) == (i - nn_max) + (j - nn_max) + v[p]) {
				a = T[p_l][1][j];
				b = T[p_r][1][i];

				// Offset upstream 
				//
				//e = (v[p] + (i - MAX_N)+ (j - MAX_N));
				//r = a + b + (e) * (e);

				// current charge is upstreamed.
				//
				r = a + b;
			}
			else
			{
				r = NINF;
			}
			if (r > max_a) {
				max_a = r;
			}
		}
	}
	return max_a;
}


void GetStudentName(std::string& your_name)
{
   //replace the placeholders "Firstname" and "Lastname"
   //with you first name and last name 
   your_name.assign("Gregory Naisat");
}

//This is the function you need to implement.
int ComputeOptimalTreePartition()
{

}
