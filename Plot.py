# -*- coding = utf-8 -*-
# @Time: 13/08/2022 21:44
# @Author: Ziqi Han
# @Student ID: 201568748
# @File: open.py
# @Software: PyCharm
import json
import jsonpath
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

files = []


def meanConfidenceInterval(dataPackage):
    confidence = 0.95
    toCalculate = []
    hTotal = []
    unPack1 = dataPackage[0]
    unPack2 = dataPackage[1]
    unPack3 = dataPackage[2]
    for i in range(0,100):
        toCalculate.append(unPack1[i])
        toCalculate.append(unPack2[i])
        toCalculate.append(unPack3[i])
        a = 1.0 * np.array(toCalculate)
        n = len(a)
        se = scipy.stats.sem(a)
        h = se * scipy.stats.t.ppf((1 + confidence) / 2., n - 1)
        toCalculate.clear()
        hTotal.append(h)
        del a,n,se,h
    return hTotal


def openFile(gameSelect):
    print("Welcome to use Plot Program, Please insert the Number of the file. ")
    fileSelect = input("Your file Number: ")
    path = '/Users/ziqi/pymarl/results/sacred/' + fileSelect + '/info.json'
    with open(path, 'r', encoding='utf-8') as fileOpen:
        jsonObj = json.load(fileOpen)
        # files.append(jsonObj)
        qTakenMean = jsonpath.jsonpath(jsonObj, '$.q_taken_mean[*]', result_type='VALUE')
        testEpLengthMean = jsonpath.jsonpath(jsonObj, '$.test_ep_length_mean[*]', result_type='VALUE')
        testReturnMean = jsonpath.jsonpath(jsonObj, '$.test_return_mean..value', result_type='VALUE')
        # print(len(qTakenMean))
        # print(len(testEpLengthMean))
        # print(type(testReturnMean))
        if gameSelect == "MG":
            return qTakenMean
        elif gameSelect == "PP":
            return testEpLengthMean, testReturnMean

    #     print(q_taken_mean)
    #     print(test_ep_length_mean)
    #     print(test_return_mean)
    #     print(len(q_taken_mean))
    # print(type(files))


def pltDiagramMG(package1):
    for j in range(1, 13):
        if j == 3:
            qTakenMeanVdn1 = package1[0:3]
            h1 = meanConfidenceInterval(qTakenMeanVdn1)
            qTakenMeanVdnMean = (np.array(qTakenMeanPackage[0]) + np.array(qTakenMeanPackage[1]) + np.array(
                qTakenMeanPackage[2])) / 3
        if j == 6:
            qTakenMeanQmix1 = package1[3:6]
            h2 = meanConfidenceInterval(qTakenMeanQmix1)
            qTakenMeanQmixMean = (np.array(qTakenMeanPackage[3]) + np.array(qTakenMeanPackage[4]) + np.array(
                qTakenMeanPackage[5])) / 3
        if j == 9:
            qTakenMeanVdnLenient = package1[6:9]
            h3 = meanConfidenceInterval(qTakenMeanVdnLenient)
            qTakenMeanVdnLenientMean = (np.array(qTakenMeanPackage[6]) + np.array(qTakenMeanPackage[7]) + np.array(
                qTakenMeanPackage[8])) / 3
        if j == 12:
            qTakenMeanQmixLenient = package1[9:12]
            h4 = meanConfidenceInterval(qTakenMeanQmixLenient)
            qTakenMeanQmixLenientMean = (np.array(qTakenMeanPackage[9]) + np.array(qTakenMeanPackage[10]) + np.array(
                qTakenMeanPackage[11])) / 3

    fig = plt.figure(num=1, figsize=(24, 8))
    xAxisVdn = np.arange(1, len(package1[0]) + 1)  # vdn
    xAxisQmix = np.arange(1, len(package1[1]) + 1)  # qmix
    ax1 = fig.add_subplot(121)
    ax1.plot(xAxisVdn, qTakenMeanVdnMean, label="VDN 1", color="r")
    ax1.plot(xAxisVdn, qTakenMeanVdnLenientMean, label="VDN 2", color ="b")
    ax1.fill_between(xAxisVdn, (qTakenMeanVdnMean - h1), (qTakenMeanVdnMean + h1), color='r', alpha=0.2)
    ax1.fill_between(xAxisVdn, (qTakenMeanVdnLenientMean - h3), (qTakenMeanVdnLenientMean + h3), color='b', alpha=0.2)
    ax1.axhline(0.0, linestyle='--', c='grey')
    ax1.set_ylim(-6, 6)
    ax1.tick_params(direction="inout", length=10, width=2, color="r", labelsize=22)
    ax1.set_xlabel("t_Max (Thousands)", fontsize=28)  # 添加x轴坐标标签
    ax1.set_ylabel("Q taken Mean", fontsize=28)  # 添加y轴标签
    ax1.set_title("VDN", fontsize=30, fontweight='bold',
                  verticalalignment="center")  # 标题（表头）
    ax1.legend(loc='upper left', fontsize='22', shadow=True)

    ax2 = fig.add_subplot(122)
    ax2.plot(xAxisQmix, qTakenMeanQmixMean, label="QMIX 1", color="r")
    ax2.plot(xAxisQmix, qTakenMeanQmixLenientMean, label="QMIX 2", color="b")
    ax2.fill_between(xAxisQmix, (qTakenMeanQmixMean - h2), (qTakenMeanQmixMean + h2), color='r', alpha=0.2)
    ax2.fill_between(xAxisQmix, (qTakenMeanQmixLenientMean - h4), (qTakenMeanQmixLenientMean + h4), color='b', alpha=0.2)
    ax2.axhline(0.0, linestyle='--', c='grey')
    ax2.set_ylim(-6, 6)
    ax2.tick_params(direction="inout", length=10, width=2, color="r", labelsize=22)
    ax2.set_xlabel("t_Max (Thousands)", fontsize=28)  # 添加x轴坐标标签
    ax2.set_ylabel("Q taken Mean", fontsize=28)  # 添加y轴标签
    ax2.set_title("QMIX", fontsize=30, fontweight='bold',
                  verticalalignment="center")  # 标题（表头）
    ax2.legend(loc='upper left', fontsize='22', shadow=True)
    plt.show()


def pltDiagramPP(testEpLengthMeanPack, testReturnMeanPack):
    for j in range(1,17):
        if j == 3:
            testEpLengthMeanVdn1 = testEpLengthMeanPack[0:3]
            testReturnMeanVdn1 = testReturnMeanPack[0:3]
            h1 = meanConfidenceInterval(testEpLengthMeanVdn1)
            testEpLengthMeanVdnMean = (np.array(testEpLengthMeanPack[0]) + np.array(testEpLengthMeanPack[1]) + np.array(
                testEpLengthMeanPack[2])) / 3
            h2 = meanConfidenceInterval(testReturnMeanVdn1)
            testReturnMeanVdnMean = (np.array(testReturnMeanPack[0]) + np.array(testReturnMeanPack[1]) + np.array(
                testReturnMeanPack[2])) / 3
        if j == 6:
            testEpLengthMeanQmix1 = testEpLengthMeanPack[3:6]
            testReturnMeanQmix1 = testReturnMeanPack[3:6]
            h3 = meanConfidenceInterval(testEpLengthMeanQmix1)
            testEpLengthMeanQmixMean = (np.array(testEpLengthMeanPack[3]) + np.array(testEpLengthMeanPack[4]) + np.array(
                testEpLengthMeanPack[5])) / 3
            h4 = meanConfidenceInterval(testReturnMeanQmix1)
            testReturnMeanQmixMean = (np.array(testReturnMeanPack[3]) + np.array(testReturnMeanPack[4]) + np.array(
                testReturnMeanPack[5])) / 3
        if j == 9:
            testEpLengthMeanVdnLenient = testEpLengthMeanPack[6:9]
            testReturnMeanVdnLenient = testReturnMeanPack[6:9]
            h5 = meanConfidenceInterval(testEpLengthMeanVdnLenient)
            testEpLengthMeanVdnLenientMean = (np.array(testEpLengthMeanPack[6]) + np.array(testEpLengthMeanPack[7]) + np.array(
                testEpLengthMeanPack[8])) / 3
            h6 = meanConfidenceInterval(testReturnMeanVdnLenient)
            testReturnMeanVdnLenientMean = (np.array(testReturnMeanPack[6]) + np.array(testReturnMeanPack[7]) + np.array(
                testReturnMeanPack[8])) / 3
        if j == 12:
            testEpLengthMeanQmixLenient = testEpLengthMeanPack[9:12]
            testReturnMeanQmixLenient = testReturnMeanPack[9:12]
            h7 = meanConfidenceInterval(testEpLengthMeanQmixLenient)
            testEpLengthMeanQmixLenientMean = (np.array(testEpLengthMeanPack[9]) + np.array(testEpLengthMeanPack[10]) + np.array(
                testEpLengthMeanPack[11])) / 3
            h8 = meanConfidenceInterval(testReturnMeanQmixLenient)
            testReturnMeanQmixLenientMean = (np.array(testReturnMeanPack[9]) + np.array(testReturnMeanPack[10]) + np.array(
                testReturnMeanPack[11])) / 3

    fig = plt.figure(num=1, figsize=(24, 20))
    xAxisVdn = np.arange(1, len(testEpLengthMeanVdnMean) + 1)
    xAxisQmix = np.arange(1, len(testEpLengthMeanQmixMean) + 1)
    ax1 = fig.add_subplot(221)
    ax1.plot(xAxisVdn, testEpLengthMeanVdnMean, label="VDN 1",  color="r")
    ax1.plot(xAxisVdn, testEpLengthMeanVdnLenientMean, label="VDN 2", color="b")
    ax1.fill_between(xAxisVdn, (testEpLengthMeanVdnMean - h1), (testEpLengthMeanVdnMean + h1), color='r',
                     alpha=0.2)
    ax1.fill_between(xAxisVdn, (testEpLengthMeanVdnLenientMean - h5), (testEpLengthMeanVdnLenientMean + h5), color='b',
                     alpha=0.2)
    ax1.axhline(0.0, linestyle='--', c='grey')
    ax1.set_ylim(-25, 225)
    ax1.tick_params(direction="inout", length=10, width=2, color="r", labelsize=22)
    ax1.set_xlabel("t_Max (10k)", fontsize=28)  # 添加x轴坐标标签
    ax1.set_ylabel("test_ep_length_mean", fontsize=28)  # 添加y轴标签
    ax1.set_title("test_ep_length_mean VDN", fontsize=30, fontweight='bold', verticalalignment="center")  # 标题（表头）
    ax1.legend(loc='upper right', fontsize='22', shadow=True)

    ax2 = fig.add_subplot(222)
    ax2.plot(xAxisQmix, testEpLengthMeanQmixMean, label="QMIX 1",  color="r")
    ax2.plot(xAxisQmix, testEpLengthMeanQmixLenientMean, label="QMIX 2",  color="b")
    ax2.fill_between(xAxisQmix, (testEpLengthMeanQmixMean - h3), (testEpLengthMeanQmixMean + h3), color='r',
                     alpha=0.2)
    ax2.fill_between(xAxisQmix, (testEpLengthMeanQmixLenientMean - h7), (testEpLengthMeanQmixLenientMean + h7), color='b',
                     alpha=0.2)
    ax2.axhline(0.0, linestyle='--', c='grey')
    ax2.set_ylim(-25, 225)
    ax2.tick_params(direction="inout", length=10, width=2, color="r", labelsize=22)
    ax2.set_xlabel("t_Max (10k)", fontsize=28)  # 添加x轴坐标标签
    ax2.set_ylabel("test_ep_length_mean", fontsize=28)  # 添加y轴标签
    ax2.set_title("test_ep_length_mean QMIX", fontsize=30, fontweight='bold', verticalalignment="center")  # 标题（表头）
    ax2.legend(loc='upper right', fontsize='22', shadow=True)

    ax3 = fig.add_subplot(223)
    ax3.plot(xAxisVdn, testReturnMeanVdnMean, label="VDN 1", color="r")
    ax3.plot(xAxisVdn, testReturnMeanVdnLenientMean, label="VDN 2", color="b")
    ax3.fill_between(xAxisVdn, (testReturnMeanVdnMean - h2), (testReturnMeanVdnMean + h2), color='r', alpha=0.2)
    ax3.fill_between(xAxisVdn, (testReturnMeanVdnLenientMean - h6), (testReturnMeanVdnLenientMean + h6), color='b', alpha=0.2)
    ax3.axhline(40.0, linestyle='--', c='grey')
    ax3.set_ylim(-10, 60)
    ax3.tick_params(direction="inout", length=10, width=2, color="r", labelsize=22)
    ax3.set_xlabel("t_Max (10k)", fontsize=28)  # 添加x轴坐标标签
    ax3.set_ylabel("test_return_mean", fontsize=28)  # 添加y轴标签
    ax3.set_title("test_return_mean VDN", fontsize=30, fontweight='bold', verticalalignment="center")  # 标题（表头）
    ax3.legend(loc='lower right', fontsize='22', shadow=True)

    ax4 = fig.add_subplot(224)
    ax4.plot(xAxisQmix, testReturnMeanQmixMean, label="QMIX 1", color="r")
    ax4.plot(xAxisQmix, testReturnMeanQmixLenientMean, label="QMIX 2", color="b")
    ax4.fill_between(xAxisQmix, (testReturnMeanQmixMean - h4), (testReturnMeanQmixMean + h4), color='r', alpha=0.2)
    ax4.fill_between(xAxisQmix, (testReturnMeanQmixLenientMean - h8), (testReturnMeanQmixLenientMean + h8), color='b', alpha=0.2)
    ax4.axhline(40.0, linestyle='--', c='grey')
    ax4.set_ylim(-10, 60)
    ax4.tick_params(direction="inout", length=10, width=2, color="r", labelsize=22)
    ax4.set_xlabel("t_Max (10k)", fontsize=28)  # 添加x轴坐标标签
    ax4.set_ylabel("test_return_mean", fontsize=28)  # 添加y轴标签
    ax4.set_title("test_return_mean QMIX", fontsize=30, fontweight='bold', verticalalignment="center")  # 标题（表头）
    ax4.legend(loc='lower right', fontsize='22', shadow=True)
    plt.show()


if __name__ == "__main__":
    print("Please Select your Game, 1 for MatrixGame, 2 for StagHunt (aka Predator Prey)")
    gameSelect = input("Your Game is: ")
    if gameSelect == "1":
        print("Please MAKE SURE the sequence of your entered value is VDN1,VDN2,VDN3,QMIX1,QMIX2,QMIX3")
        qTakenMeanPackage = []
        for i in range(1, 13):
            q_taken_mean = openFile(gameSelect="MG")
            q_taken_mean = q_taken_mean[0:100]
            qTakenMeanPackage.append(q_taken_mean)
        pltDiagramMG(qTakenMeanPackage)
    elif gameSelect == "2":
        print("Please MAKE SURE the sequence of your entered value is VDN1,VDN2,VDN3,QMIX1,QMIX2,QMIX3,LV1,LV2,LV3,LQ1,LQ2,LQ3")
        testEpLengthMeanPackage = []
        testReturnMeanPackage = []
        for i in range(1, 13):
            test_ep_length_mean, test_return_mean = openFile(gameSelect="PP")
            testEpLengthMeanPackage.append(test_ep_length_mean)
            testReturnMeanPackage.append(test_return_mean)
        pltDiagramPP(testEpLengthMeanPackage, testReturnMeanPackage)
