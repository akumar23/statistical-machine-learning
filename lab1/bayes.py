import numpy 
import scipy.io 
import math 
import geneNewData 
import matplotlib 
import scipy # import required libraries from scipy import stats from math import exp,sqrt

def main(): 
    myID='0000' 
    geneNewData.geneData(myID) 
    Numpyfile0 = scipy.io.loadmat('digit0_stu_train'+myID+'.mat') 
    Numpyfile1 = scipy.io.loadmat('digit1_stu_train'+myID+'.mat') 
    Numpyfile2 = scipy.io.loadmat('digit0_testset'+'.mat') 
    Numpyfile3 = scipy.io.loadmat('digit1_testset'+'.mat') 
    train0 = Numpyfile0.get('target_img') 
    train1 = Numpyfile1.get('target_img') 
    test0 = Numpyfile2.get('target_img') 
    test1 = Numpyfile3.get('target_img') 
    print([len(train0),len(train1),len(test0),len(test1)]) 
    print('Your trainset and testset are generated successfully!')

    feature1_0 = [] 
    feature2_0 = [] 
    feature1_1 = [] 
    feature2_1 = [] 

    for i in range(5000): 
        feature1_0.append(numpy.average(train0[i])) 
        feature2_0.append(numpy.std(train0[i])) 
        feature1_1.append(numpy.average(train1[i])) 
        feature2_1.append(numpy.std(train1[i])) 
        
    feature1_0_Ar = numpy.array(feature1_0) 
    feature2_0_Ar = numpy.array(feature2_0) 
    feature1_1_Ar = numpy.array(feature1_1) 
    feature2_1_Ar = numpy.array(feature2_1) 
        
    print("\n Train set results")  
    print(feature1_0_Ar.mean()) 
    print(feature1_0_Ar.var()) 
    print(feature2_0_Ar.mean()) 
    print(feature2_0_Ar.var()) 
    print(feature1_1_Ar.mean()) 
    print(feature1_1_Ar.var()) 
    print(feature2_1_Ar.mean()) 
    print(feature2_1_Ar.var()) 
        
    f1_test0 = [] 
    f2_test0 = [] 
    f1_test1 = [] 
    f2_test1 = [] 
        
    for i in range(980): 
        f1_test0.append(numpy.average(test0[i])) 
        f2_test0.append(numpy.std(test0[i])) 
        f1_test1.append(numpy.average(test1[i])) 
        f2_test1.append(numpy.std(test1[i])) 

    f1_test0_Ar = numpy.array(f1_test0) 
    f2_test0_Ar = numpy.array(f2_test0) 
    f1_test1_Ar = numpy.array(f1_test1) 
    f2_test1_Ar = numpy.array(f2_test1) 

    print("\n Now test set results") 
    print(f1_test0_arr.mean()) 
    print(f1_test0_arr.var()) 
    print(f2_test0_arr.mean()) 
    print(f2_test0_arr.var()) 
    print(f1_test1_arr.mean()) 
    print(f1_test1_arr.var()) 
    print(f2_test1_arr.mean()) 
    print(f2_test1_arr.var()) 
    print("\n calculate gaussian formula pdf and get posterior probabilities abnd compare and get results") 
    
    test0_digit0 = 0 
    test0_digit1 = 0 
    test1_digit0 = 0 
    test1_digit1 = 0 
    f1_mean_test1 = f1_test1_arr.mean() 
    f1_var_test1 = f1_test1_arr.var() 
    f1_std_test1 = f1_test1_arr.std() 
    f2_mean_test1 = f2_test1_arr.mean() 
    f2_var_test1 = f2_test1_arr.var() 
    f2_std_test1 = f2_test1_arr.std() 
    f1_mean_test0 = f1_test0_arr.mean() 
    f1_var_test0 = f1_test0_arr.var() 
    f1_std_test0 = f1_test0_arr.std() 
    f2_mean_test0 = f2_test0_arr.mean() 
    f2_var_test0 = f1_test0_arr.var() 
    f2_std_test0 = f2_test0_arr.std() 
    
    for i in range(980): 
        prob_X_given_digit1 = scipy.stats.norm.pdf(test0[i], loc=f1_mean_test1, scale=f1_std_test1) * stats.norm.pdf(test0[i], loc=f2_mean_test1, scale=f2_std_test1) * 0.5 
        prob_X_given_digit0 = scipy.stats.norm.pdf(test0[i], loc=f1_mean_test0, scale=f1_std_test0) * stats.norm.pdf(test0[i], loc=f2_mean_test0, scale=f2_std_test0) * 0.5 
        if prob_X_given_digit1 > prob_X_given_digit0: 
            test0_digit1 += 1 
        else: 
            test0_digit0 += 1 
        i += 1 
    
    for i in range(1135): 
        prob_X_given_digit1 = scipy.stats.norm.pdf(test1[i], loc=f1_mean_test1, scale=f1_std_test1) * stats.norm.pdf(test1[i], loc=f2_mean_test1, scale=f2_std_test1) * 0.5 
        prob_X_given_digit0 = scipy.stats.norm.pdf(test1[i], loc=f1_mean_test0, scale=f1_std_test0) * stats.norm.pdf(test1[i], loc=f2_mean_test0, scale=f2_std_test0) * 0.5 
        
        if prob_X_given_digit1 > prob_X_given_digit0: 
            test0_digit1 += 1 
        else: 
            test0_digit0 += 1 
        i += 1 
    
    accuracy_score0 = test0_digit0/(test0_digit1+test0_digit0) 
    accuracy_score1 = test0_digit1/(test0_digit1+test0_digit0) 
    print(accuracy_score0) 
    print(accuracy_score1) 
    
if __name__ == '__main__': 
    main()