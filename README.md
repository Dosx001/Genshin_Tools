# Genshin_Tools
Genshin Tools is a website hosting an array of tools to enhance the player expirence of Genshin Impact players.

# Table of Contents
* [Functional](#functional)
    * [Pity Counter](#pity-counteer)
    * [Random Event](#random-event)
* [In Production](#in-production)
    * [Quest Log](#quest-log)
* [Concept](#concept)
    * [Timers](#timers)
    * [Resource Manger](#resource-manager)
    * [Resource Converter](#resource-converter)

# Functional

## Pity Counter
The Pity Counter page keeps track of users’ number of wishes made for each banner. Users can increase the counter by using the “+1” or “+10” button. The counters will also automatically reset when users hit pity, at 90 wishes for Character and Standard banner and 80 for the Weapon Banner. If users pull a 5-star item in-game, then users can reset their Genshin Tools pity counter to 0 by using the “Reset” button. Users can use the “Report” button to display the number of days until pity, the date when the user hits pity, the number of primogems needed for pity, and the minimum price of the primogems. The report assumes the user plays every day, completes their daily commissions, and claims their daily rewards. If users have the Blessing of the Welkin Moon (BotWM) then users can check the BotWN check box, then their report will take into account the BotWM. If users have primogems in their in-game inventory they can also input them into the Pity Counter page, and the report will take account of their primogems for their report.

<p align="center">
    Pity Counter Page
</p>

![pity counter](https://i.imgur.com/o0RY8vq.png)

<p align="center">
    In-game Character Banner
</p>

![banner](https://i.imgur.com/bVaZd0V.png)

## Random Event
The Random Event page keeps track of the daily number of in-game [Random Events](https://genshin-impact.fandom.com/wiki/Random_Event) left. Users can subtract one from the counter using the “-1” button. The counter resets every 24 hours. The page also features a video guide on how to effectively complete Random Events.

<p align="center">
    Random Event Page
</p>

![random event](https://i.imgur.com/cLEKORj.png)

Future implementation of the Random Event page will allow users to pick a time zone to allow the counter to reset at the appropriate time.

# In Production

## Quest Log
Genshin Impact has many and different types of quests and many of these quests have requirements to start them such as other quests. Some of the quests’ requirements are strictly RNG. The Quest Log page is designed to keep track of players’ quest completion. The Quest Log page also offers quick and useful information for each quest. For example, the location of the quest, the NPC to start the quest, and the requirements such as Adventure Rank, Archon quest, World quest, or Commission. 

<p align="center">
    Quest Log Page
</p>

![quest log](https://i.imgur.com/aiVmuHZ.png)

# Concept

## Timers
Many resources in Genshin Impact have 24, 48, or 72 hours respawn rates. Having timers will allow users to farm for resources more effectively. Users would be able to set a 24, 48, or 72 hour timer that counts down. Users will be able to set an icon to the timer to distinguish which resource the timer is designated to. Also, the timer would be nameable to help users give a location or any useful information to the timer.

<p align="center">
    Timer
    <div align="center">
        <img src="https://i.imgur.com/z1jRxSO.png">
    </div>
</p>

## Resource Converter
Genshin Impact has resources called ascension materials that are heavily time gated and difficult to gather. Genshin Impact also allows players to convert lower tier materials to higher tier materials, for example 3 fragments = 1 shard, 3 shards = 1 chuck, 3 chucks = 1 gem. The resource converter page would allow users to input their current inventory and the page would display summary of the total number of runs, resin, and days needed based on different drop rates and world levels.

<p align="center">
    Summary
    <div align="center">
        <img style="right:0 " src="https://i.imgur.com/C6szWzN.png?2">
        <img style="right:0 " src="https://i.imgur.com/EQKKaH2.png?1">
        <img style="right:0 " src="https://i.imgur.com/AmVlgfN.png?1">
    </div>
</p>

## Resource Manager
The Resource Manager page will keep track of users’ character ascensions, weapon ascensions and talent levels. The page will also display a weekly schedule on what to farm based on users’ data. This tool will help players because these ascension materials are on a daily rotation. Having a weekly schedule would allow players to know what to farm and will streamline the players’ progression in Genshin Impact. 