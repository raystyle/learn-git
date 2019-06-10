OOP_Polymorphism_using_interface.md

使用接口实现多态

一个类型如果定义了接口的所有方法，那它就**隐式**地实现了该接口。

所有实现了接口的类型，都可以把它的值保存在一个**接口类型的变量**中。在 Go 中，我们使用接口的这种特性来实现多态。

新增收益流

假设前面的组织通过广告业务，建立了一个新的收益流（Income Stream）。我们可以看到添加它非常简单，

并且计算总收益也很容易，我们无需对 calculateNetIncome 函数进行任何修改。这就是多态的好处。

```go
package main

import (
    "fmt"
)

type Income interface {
    calculate() int
    source() string
}

type FixedBilling struct {
    projectName  string
    biddedAmount int
}

type TimeAndMaterial struct {
    projectName string
    noOfHours   int
    hourlyRate  int
}

type Advertisement struct {
    adName     string
    CPC        int
    noOfClicks int
}

func (fb FixedBilling) calculate() int {
    return fb.biddedAmount
}

func (fb FixedBilling) source() string {
    return fb.projectName
}

func (tm TimeAndMaterial) calculate() int {
    return tm.noOfHours * tm.hourlyRate
}

func (tm TimeAndMaterial) source() string {
    return tm.projectName
}

func (a Advertisement) calculate() int {
    return a.CPC * a.noOfClicks
}

func (a Advertisement) source() string {
    return a.adName
}

func calculateNetIncome(ic []Income) {
    var netincome int = 0
    for _, income := range ic {
        fmt.Printf("Income From %s = $%d\n", income.source(), income.calculate())
        netincome += income.calculate()
    }
    fmt.Printf("Net income of organisation = $%d", netincome)
}

func main() {
    project1 := FixedBilling{projectName: "Project 1", biddedAmount: 5000}
    project2 := FixedBilling{projectName: "Project 2", biddedAmount: 10000}
    project3 := TimeAndMaterial{projectName: "Project 3", noOfHours: 160, hourlyRate: 25}
    bannerAd := Advertisement{adName: "Banner Ad", CPC: 2, noOfClicks: 500}
    popupAd := Advertisement{adName: "Popup Ad", CPC: 5, noOfClicks: 750}
    incomeStreams := []Income{project1, project2, project3, bannerAd, popupAd}
    calculateNetIncome(incomeStreams)
}
```