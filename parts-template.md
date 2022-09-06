
<!--` parts1 -->
# Parts

Parts are the smallest way of describing anything in the ODM. Think of the example of parts of a car. If you own a car, your garage can access a parts list that contains every part of your car -- right down to every nut and bolt. The same is true for the ODM.

The ODM has a part ID (partID) and part description (partDescription) for every measure, method and attribute. There are also partIDs for measure categories, units, aggreations, and other parts. Below is the part list.

<!--` parts1/ -->

```{rvml}```
var versionText = <!--` versionText -->Version first released: <!--` versionText/ -->
var updateText = <!--` updateText -->Version last updated: <!--` updateText/ -->

var tableRow = {**{{like:("label_%")}}**, ({{partID}}) ,(#{{partID}}), {{partDescription}},".<br /> like:("Instruction_%")", {{like:("Instruction_%")}}," <br /> like:("Part Type_%")",
 {{like:("Part Type_%")}}, "<br />like:("Status_%")", {{like:("Status_%")}}, versionText ,{{firstReleased}}, updateText, {{lastUpdated}},"<br /> like:("Data type_%")", {{like:("Data type_%")}}}

{{filter:*, order:label = ASC ,format(tableRow)}}

```{rvml}```
