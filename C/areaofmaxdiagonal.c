int areaOfMaxDiagonal(int** dimensions, int dimensionsSize, int* dimensionsColSize) {
    int MaxDiag = 0;
    int MaxArea = 0;
    int cur_dia = 0;
    int cur_are = 0;

    for (int i = 0 ; i < dimensionsSize; i++){
        cur_dia = (dimensions[i][0] * dimensions[i][0]) + (dimensions[i][1] * dimensions[i][1]);  
        cur_are = (dimensions[i][0] * dimensions[i][1]);   

        if ((cur_dia > MaxDiag) || (cur_dia == MaxDiag && cur_are >= MaxArea )){
            MaxDiag = cur_dia;
            MaxArea = cur_are;
        } 
    }
    return MaxArea;    
}