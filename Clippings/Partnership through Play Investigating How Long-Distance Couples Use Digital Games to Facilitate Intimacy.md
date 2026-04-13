---
title: "Partnership through Play: Investigating How Long-Distance Couples Use Digital Games to Facilitate Intimacy"
source: "https://arxiv.org/html/2505.09509?_immersive_translate_auto_translate=1"
author:
published:
created: 2026-04-13
description:
tags:
  - "clippings"
---
by

Nisha Devasia [ndevasia@uw.edu](mailto:ndevasia@uw.edu) University of WashingtonSeattleWashingtonUSA, Adrian Rodriguez [aarod@uw.edu](mailto:aarod@uw.edu), Logan Tuttle [logan347@uw.edu](mailto:logan347@uw.edu) University of WashingtonSeattleWashingtonUSA and Julie A. Kientz [jkientz@uw.edu](mailto:jkientz@uw.edu) University of WashingtonSeattleWashingtonUSA

(2025)

###### Abstract.

Long-distance relationships (LDRs) have become more common in the last few decades, primarily among young adults pursuing educational or employment opportunities. A common way for couples in LDRs to spend time together is by playing multiplayer video games, which are often a shared hobby and therefore a preferred joint activity. However, games are relatively understudied in the context of relational maintenance for LDRs. In this work, we used a mixed-methods approach to collect data on the experiences of 13 couples in LDRs who frequently play games together. We investigated different values around various game mechanics and modalities and found significant differences in couple play styles, and also detail how couples appropriate game mechanics to express affection to each other virtually. We also created prototypes and design implications based on couples’ needs surrounding the lack of physical sensation and memorabilia storage in most popular games.

Video games, Long-distance relationships, Relational maintenance, Design prototyping

## 1\. Introduction

The prevalence of long-distance relationships (LDRs) between romantic couples is believed to have increased significantly over the past few decades [^76], typically due to the pursuit of educational or employment opportunities [^62]. An estimated 25-50% of American college students are believed to be in LDRs [^56], and millions of married adults choose to live apart and maintain separate homes for the purpose of career advancement [^67]. Research has shown that couples in LDRs have comparable levels of relationship satisfaction to geographically close relationships (GCRs) [^29] and are equally likely to last [^40]. However, LDRs face challenges caused by a lack of co-location, such as inconsistent communication [^70], limited face-to-face contact [^27], lack of intimate physical contact [^60], and higher levels of relationship stress compared to GCRs [^33].

Increased usage of social media platforms has made it possible to maintain constant lines of communication across long distances [^47] [^41] [^60]. These forms of computer-mediated communication (CMC) - human communication through the use of two or more electronic devices [^81] - have become key tools for relational maintenance in LDRs, allowing couples to communicate in real time through instant messaging or face-to-face contact through video calling platforms. In particular, CMC enables couples to engage in leisure activities together, such as watching movies [^87] or playing games [^5]. Engaging in joint leisure activities as a couple has been shown to increase perceived relationship quality [^16] [^17] [^77].

In particular, playing games together is an increasingly common way to keep in touch with friends and romantic partners over long distances [^5] [^26] [^36]. However, digital games are relatively understudied for the maintenance of romantic relationships [^36] when compared to research on socialization with friends and family [^19] [^22] [^55] [^61], or on gaming as a coping mechanism during difficult life periods [^9] [^46] [^57]. These works discuss close relationships generally, and do not focus on romantic relationships. This is a notable gap in the field; particularly for young adults, romantic relationships are believed to have higher emotional valence than other close or familial relationships, and play a more significant role in emotional well-being [^6]. Furthermore, while ”couple technologies” have been a longstanding design space in HCI [^12], the majority of these artifacts were strictly designed for research settings [^43]. They do not reflect more realistic communication practices used between couples, or activities that are already integrated into people’s lifestyles, such as games [^59]. In this work, we attempt to fill this gap by understanding how couples in LDRs use digital games as mediums of connection within their relationship. To this end, we posed the following research questions:

- RQ1: How do different features and modalities of digital games afford the promotion of intimacy and closeness between long-distance partners?
- RQ2: What interpersonal strategies do long-distance partners use while gaming to feel closer to each other?
- RQ3: How can these insights inform the design of technologies created specifically for long-distance couples?

To explore these questions, we conducted a diary study, employed semi-structured interviews, and engaged in a design activity with 13 couples in LDRs to gain a comprehensive understanding of their experiences playing games together. The diaries and interviews explored the interplay of social dynamics between couples and their friends, benefits and drawbacks of different game modalities and mechanics, and used [^43] ’s strategies for designing technologies for long-distance connection to frame couples’ gaming preferences. Through a combination of inductive and deductive analysis, we extracted key themes surrounding the affordances of cooperative vs. competitive multiplayer games, the liminality between in-person and in-game social interactions, and the appropriation of game mechanics to express affection. We developed couple archetypes to inform possible future game design interventions specifically targeted at couples in LDRs (e.g. [^64]), and prototyped solutions around couples’ identified limitations in current game designs. We contribute a comprehensive mixed-methods, empirical understanding of how couples in LDRs are using digital games as a form of relational maintenance.

## 2\. Related Work

### 2.1. Games and Relational Maintenance

Although scholars have proposed several definitions for relational maintenance (e.g. [^34] [^32] [^77], all share the common theme that certain types of interactions and behaviors function to preserve ongoing relationships. Relational maintenance is used to support relationships between friends, family members, and romantic partners. However, romantic partners face particular communication challenges that platonic or familial relationships do not, and must coordinate shared commitment and life plans in addition to navigating the challenges of everyday life together [^73]. To combat this, romantic partners engage in various relational maintenance strategies, which [^77] ’s oft-cited conceptualization defines as: open communication, positivity, assurances, sharing tasks, and joint social interactions with friends. The advent of computer-mediated communication (CMC) brought about various networked social technologies, which are now commonly used as mediums of relational maintenance for both co-located and long-distance relationships [^82]. Messaging platforms such as email, WhatsApp, and text messaging provide communication partners with ”speed, relative privacy, \[and\] decentralization” [^10], while social media and microblogging platforms such as Facebook, Twitter, and Instagram foster interactivity and connectivity with friends and strangers alike [^75] [^84] [^65]. Patterns of interaction remain similar between in-person and online communication: participating in the aforementioned relational maintenance strategies during CMC was shown to positively correlate with relationship satisfaction [^74] [^4]. However, while communication is crucial to the success of any romantic relationship, it is particularly true for long-distance relationships, where in-person interactions are limited [^28] [^41].

Studies on relational maintenance have prioritized the investigation of romantic relationships over familial connections or friendships [^82]. Conversely, gaming as a method of maintaining friendships has been relatively well studied [^19] [^22] [^55]. [^30] found that cooperative and interdependent mechanics can promote social closeness between strangers in multiplayer games. Openness towards social connection, frequency of offline communication, and physical/social proximity have all been found to predict relational closeness in online gaming spaces [^55] [^83]. Indeed, games are often extensions of pre-existing offline relationships (e.g. friends, family, spouses, co-workers [^71]) as opposed to isolated virtual experiences [^90], serving as ”third places” [^79] where players can regularly gather to socialize and maintain their connections. However, many of these findings are general to close relationships and do not address how games can serve as relational maintenance in the face of aforementioned challenges specific to romantic relationships [^73]. Indeed, engaging in shared leisure activities, such as games, is positively correlated to relationship satisfaction [^17]. Furthermore, playing games together can involve all five of [^76] ’s strategies, and we use this typology as a lens to explore how partners use games to stay connected across distances.

### 2.2. Gaming During Difficult Life Experiences

Games can serve as a much needed respite from stressful circumstances [^46]. They are often used as a form of escapism, which [^52] define as the avoidance of reality to allow for emotional regulation, mood management, recovery, and coping. These ”four pillars” have all been explored (e.g. emotional regulation for adults [^11] [^18] and adolescents [^37]; mood management [^68]; and recovery [^66] [^25]), but particularly extensive research was conducted on gaming as a coping mechanism during the COVID-19 pandemic, when many people worldwide found themselves physically distanced from their loved ones [^9] [^57] [^61] [^86] [^3] [^35]. In particular, [^9] found that players ”appropriated” commercial video games in crisis situations; although most games are not explicitly designed to support resilience or psychological recovery, players imbued games with their own meanings and developed unique usage patterns to leverage them as a support mechanism in difficult circumstances. Coping has been explored in LDRs as well; [^56] explored how couples cope with problems in an exploration of college students in LDRs, using [^7] ’s conceptualization of communication types: individual, dyadic, relationship-focused, and social support. The act of romantic partners gaming together could be viewed as a form of relationship-focused coping; however, none of the above papers have explored gaming as a coping mechanism for couples in particular.

### 2.3. Technology for Long-Distance Relationships

#### 2.3.1. Couple technologies

”Couple technologies” are a longstanding design space in HCI, and researchers have created artifacts that can transmit intimate gestures through a variety of signals [^12]. Some promote a sense of indirect awareness; for example, Feather and Scent, intended for when one partner was away on travel. Both artifacts can be activated remotely to make a feather float or release a scent of choice, indicating to the at-home partner that the traveling partner is thinking of them [^80]. A more direct example would be inPhase [^85], a system designed to provide audio signals when two users coincidentally performed the same action simultaneously. Many use light-up signals to evoke more direct sensations of awareness, such as the Virtual Intimate Object [^48], LumiTouch [^20], or Lover’s Cup [^23]. Others try to simulate physical sensation, such as Hug from a Distance [^58], inTouch [^14], or the united-pulse rings [^89]. Researchers have also devised unique mediums through which couples can communicate, such as the Cube [^38], a virtual 3D cube that allows couples to compose and send encrypted symbolic messages, or Hello There, an application in which one partner can send the other an audio message from a particular geographical location, and they will only receive the message when at that particular location themselves [^49]. However, many of these ”couple technologies” were created exclusively for research settings and are not reflective of more common methods of maintaining connection, such as video calling [^60], texting [^10], or playing games together [^36].

#### 2.3.2. Strategies for mediating relatedness

In a scoping review of artifacts designed for relatedness, [^43] identified strategies used to create and mediate six different facets of relatedness, which are: awareness (creating a feeling of continuity by sharing ambient information about current activities or moods without explicit communication between partners), expressivity (enabling expression of emotions in a wide variety of ways), physicalness (simulating secondary effects of physical proximity or meaningful gestures), gift giving (demonstrating caring and valuing through exchange of gifts), joint action (allowing for carrying out an action together), and memories (recording past activities and special moments of a relationship). Rather than defining digital games as a form of ’couple technology’, however, this work frames games as an existing medium that users ’misuse’ to show affection through various invented social practices. This phenomenon, in which couples in LDRs appropriate certain affordances of existing technologies to better suit their needs, has been previously documented in the literature. For example, [^51] document the squillo, a social practice in Italy where a friend telephones another friend but hangs up before they can answer, indicating to the receiver that the caller is thinking of them. The telephone was not designed for this use case, but a social practice was invented around its ability to ring, and both the caller and the receiver understand the meaning conveyed by a squillo. Similarly, [^60] investigated how long-distance couples appropriate various features of video calling platforms for intimate practices, such as kissing the webcam to simulate actually kissing their partner’s forehead. Building upon this line of research, this work investigates how different features of video games are appropriated to demonstrate mutual caring. In particular, we utilize [^43] ’s six facets of connectedness as a framework for analyzing play within the context of this study.

### 2.4. Playing Video Games as a Couple

While an exact estimate for how many couples play video games together does not exist, the percentage is likely large given the overall high participation rates among adults. In 2023, the Entertainment Software Association reported that an estimated 65% of all Americans play video games. Of these, 74% are adults over the age of 18 [^31]. Yet, the body of research on how romantic couples use games as a medium of connection is limited, and especially so when geographical separation is taken into account. A small amount of research documents the phenomenon of players meeting and becoming romantically involved through online games, with some leading to long-term and/or co-located relationships [^45] [^92] [^8]. Many of these couples expressed difficulties in maintaining these relationships online and over long distances [^45]. [^5] investigated how romantic couples use World of Warcraft as part of their shared leisure time; however, these couples were all co-located. [^26] investigated how games affect conflict between couples; however, in this case, only one partner actively played games, and geographical co-location was not specified. Indeed, much of the work on couples gaming together has been focused on how gaming affects relationships in which one partner (typically male) plays games frequently and the other (typically female) does not [^26] [^2] [^24]. [^71] suggested that many female players begin playing games due to male spouses or romantic partners. [^91] found significant differences in player motivations between gender, with male players prioritizing achievement and manipulation, and female players prioritizing relationships. More recently, [^63] ’s Motive Disposition Theory suggests that implicit player motivations may have a greater effect on in-game social behavior than explicit motivations. Researchers have investigated how to address such asymmetries in desired outcomes and styles of play through game design (e.g. [^42] [^39]). These asymmetries extend to relationship satisfaction; [^2] suggested that relationship satisfaction was negatively impacted when only one partner engaged in gaming, but that playing games together had a positive effect. Indeed, participating in leisure activities together has been shown to increase relationship satisfaction [^74]. To this end, [^36] used the Relational Maintenance Strategies Measure [^78] to deductively analyze couples’ survey responses regarding their experiences playing League of Legends together; however, only 57.6% of couples reported being in long-distance relationships. A further limitation of the current body of research is that many of these works are focused on specific games, and are limited primarily to the study of Massively Multiplayer Online Role Playing Games (MMORPGs). This work intends to generalize across broad features of games from many genres that couples play together, rather than investigate dynamics within a particular game. Additionally, we seek to address the difficulties expressed by couples who maintain the majority of their relationship through games due to geographical separation [^45].

## 3\. Methods

To understand the experiences of long-distance couples using digital games as a medium of connection, we conducted a diary study [^69] and semi-structured interviews with 13 couples spanning a wide range of geographical separation and relationship length.

### 3.1. Participants and Recruitment

We recruited using a screener survey, which was disseminated through gaming servers at our university and posted on social media sites such as Reddit and Twitter. This survey asked basic questions about couple demographics, what games they tended to play together and how often, and how they felt playing games affected their relationship. Inclusion criteria specified that participants must currently live more than 50 miles away from each other in separate residences, must be over 18 years of age, and must play games with their partners at least once a week. Of the 75 initial responses to the screening survey, 15 couples were contacted to participate in the full study. In choosing these couples, we sought a variety of age ranges and gender identities, types of games played, and a range of time zone differences. One couple did not complete any study activities past the initial onboarding, and one couple separated during the study, resulting in 13 couples who completed the entire study (see Table 1). These 13 couples had an average age of 25.2, with the majority of participants in their early to mid 20s, which is within the typical age range for long-distance relationships [^56]. They had been together for an average of 2.34 years, ranging from 2 months to as long as 8 years. Five couples had no time zone differences but lived geographically separate (e.g., Seattle and San Francisco), while other couples reported time differences of up to 19 hours (e.g., the Philippines and the USA). While six couples had at least one member outside of North America, only one couple was completely international. The majority see each other in person about once a month, but 2 couples were ‘never mets’, which means that they met and began their relationship online but had not met in person at the time the study was conducted. This phenomenon is documented in studies such as [^45], [^8], and [^92]. The 26 individuals who completed the study were each compensated with a $40 USD gift card.

Table 1. Overview of participants who completed all portions of the study

| PID | Age | Gender | Location | Relationship length | In-person meetings | Joint favorite game (Platform) |
| --- | --- | --- | --- | --- | --- | --- |
| C1A | 25 | M | USA | 6 months | Yearly | Cine2Nerdle (Browser) |
| C1B | 23 | NB | Australia |  |  |  |
| C2A | 23 | M | Seattle | 3 years | 3x a year | Splatoon 3 (Nintendo Switch) |
| C2B | 23 | F | San Francisco |  |  |  |
| C3A | 25 | F | Seattle | 2.5 years | Monthly | Scribblio (Mobile) |
| C3B | 22 | M | San Francisco |  |  |  |
| C4A | 22 | NB | USA | 3 years 4 months | Yearly | Splatoon 3 (Nintendo Switch) |
| C4B | 22 | F | United Kingdom |  |  |  |
| C5A | 24 | F | New York | 2 years | Monthly | We Were Here (Desktop) |
| C5B | 24 | M | Boston |  |  |  |
| C6A | 27 | F | Philippines | 1.5 years | 2x a year | Genshin Impact (Desktop) |
| C6B | 27 | M | USA |  |  |  |
| C7A | 24 | F | Canada | 3 years | 3x a year | Final Fantasy XIV (Desktop) |
| C7B | 27 | M | USA |  |  |  |
| C8A | 31 | F | USA (2 hour difference) | 2 months | Every few months | Stardew Valley (Desktop) |
| C8B | 27 | NB |  |  |  |  |
| C9A | 24 | NB | USA | 2 years | Only met once | Minecraft (Desktop) |
| C9B | 22 | F | Canada |  |  |  |
| C10A | 29 | F | Turkey (500 km apart) | 8 years | Every several months | Heroes of the Storm (Desktop) |
| C10B | 36 | M |  |  |  |  |
| C11A | 31 | M | USA | 5 months | Never mets | Apex Legends (Desktop) |
| C11B | 26 | F | United Kingdom |  |  |  |
| C12A | 26 | F | USA (100 miles apart) | 4 years | Monthly | Stardew Valley (Desktop) |
| C12B | 27 | M |  |  |  |  |
| C13A | 22 | M | Germany | 2 months | Never mets | Out of Space (Desktop) |
| C13B | 27 | NB | USA |  |  |  |

### 3.2. Data Collection

The data for this study was collected from February - May 2024. Participants from the initially selected 15 couples all attended a 15 minute onboarding session with the lead researcher, in which the goals of the study and the two main parts of the study (the diary study and the semi-structured interview) were explained. All participants completed a consent form approved by our institution’s Institutional Review Board (IRB) prior to the onboarding session.

#### 3.2.1. Diary Study

Participants were asked to keep a diary in which they logged a minimum of five entries each after playing a game with their partner. In the onboarding session, they were instructed to fill out the diary (provided through Google Forms) immediately after they finished playing a joint gaming session. The goal of this was to have concrete, in-the-moment examples from couples’ play sessions to probe later on in the interviews, as well as to encourage couples to reflect on their own play. Each diary entry asked the following questions:

- Today, my partner and I played the following game: \[Open-response\]
- I would describe this game in the following ways: \[Options: Cooperative, Competitive, Goal oriented, Requires a lot of grinding, Requires strategizing, Casual, Creative, Other\]
- How long did the game session last for? \[Open-response\]
- Describe some of the gameplay you engaged in today. \[Open-response\]
- While playing in today’s game session, some of the emotions I felt were: \[Open-response\]
- On a scale of 1-5, playing today made me feel: \[1: very disconnected from my partner, 5: very close to my partner\]
- Describe the most memorable part of the gameplay today and why it was memorable. \[Open-response\]

In addition, diary entries asked participants to identify which of [^43] ’s six facets of connectedness, if any, they felt applied to their game session. We adapted and simplified definitions from the original paper to position the game as the technology promoting the six facets of connectedness. They were provided to the participants as follows:

- Awareness: The game enabled me to feel a sense of continuity and presence with my partner without doing anything specific.
- Expressivity: The game enabled me to express my feeling and emotions in a wide variety of ways.
- Physicalness: The game allowed for a feeling of physical intimacy.
- Gift giving: The game gave me the ability to demonstrate caring and valuing my partner through reciprocal exchange.
- Joint action: The game allowed my partner and I to carry an action out together.
- Memories: The game allowed us to keep records of our activities and special in-game moments.

#### 3.2.2. Semi-Structured Interview

After completing their diary entries, participants engaged in a final semi-structured interview with the lead researcher, lasting around 60-75 minutes. Interviews were conducted with both members of the couple simultaneously to glean additional detail on their diary entries and overall experience gaming together. The semi-structured interview protocol was tailored to each couple’s diary entries, and questions were therefore variable across couple; however, common questions included:

- What do you like/dislike about playing cooperative/competitive games with each other?
- What sorts of topics do you discuss while gaming together?
- How does playing with friends affect the dynamic between you and your partner?
- Which of Hassenzahl’s six facets of connectedness (presented to each couple) are the most important to you in the games you play and why?
- Which facets would you like to see implemented more in games and why?

#### 3.2.3. Mechanics, Dynamics, Aesthetics Activity

![[x1.jpg|Refer to caption]]

Figure 1. A snapshot of the initial board given to participants for the MDA activity, listing examples of each component (the full list of mechanics and dynamics are not shown in this image).

At the end of the semi-structured interview, couples jointly engaged in an activity using the MDA (Mechanics, Dynamics, Aesthetics) framework. First presented by [^44] at the Game Developers Conference in the early 2000s, the MDA intends to bridge the gap between game design, criticism, and research. We chose to adapt this commonly used framework as an activity for non-experts by discretizing each component of the MDA into individual elements and presenting them to participants as a Figma board of sticky notes (see Figure 2 for what participants were initially presented with). We derived a starting set of elements from [^53], and invited participants to add their own elements as they saw fit. As suggested in [^15] ’s implementation of the MDA framework in an informal environment: ”because the player perceives the game through the lens of its aesthetics, the selection of which aesthetics should be evoked by the game makes for a useful starting point for the game developer”. Therefore, we had participants - acting as both players and designers within the scope of the activity - begin by identifying their ideal aesthetics, then mechanics, and finally dynamics. The lead researcher began the activity by presenting the Figma board to each couple and giving them 30 minutes to identify elements of an ideal game to play together, and did not participate in this activity other than answering clarifying questions about different elements. See Figure 2 for an example of a couple’s output from this activity.

![[x2.jpg|Refer to caption]]

Figure 2. An example of the output of a couple’s MDA activity. The ideal aesthetics are in red (Fantasy, Discovery), mechanics are in purple (Map, Levels, Missions, Obstacles/enemies, Items), and dynamics are in blue (Players explore virtual environment of game, Objects can be collected in no particular order, Turn-based gameplay).

### 3.3. Analysis

We conducted the semi-structured interviews over Zoom and used Zoom’s in-built audio transcription or Rev.ai to generate transcripts. The first author, along with a research group consisting of five undergraduate and masters students, performed a qualitative analysis of the interview transcripts. For the first four transcripts reviewed, the group followed the steps of [^13] ’s thematic analysis: Each member inductively open-coded the same transcript independently, and then brought their codes to the research group meeting. Researchers then made sticky notes for each individual code, and then performed an affinity diagramming exercise (also known as the KJ method [^72]) to develop themes. After four iterations, the research team reviewed and agreed upon a set of preliminary themes using a consensus model. The first author then used these preliminary themes to independently code the remainder of the transcripts. No new themes were added, but the preliminary themes were subdivided and elaborated upon with data from the additional transcripts.

We analyzed the diary entries with Microsoft Excel and wrote Python and R scripts for further statistical analysis. These results are presented as a descriptive overview in Section 4.1.

Through our analysis of the diary entries and interview transcripts, we found that the 13 couples in our study fell into three distinct categories based on how they described themselves playing games together. These archetypes are presented in Section 4.6. After developing definitions of each archetype, the first and second authors, as well as three members of the qualitative research group, independently assigned each couple to an archetype, based on their diary entries and interviews. Intercoder reliability among five raters using Fleiss’ kappa was calculated as 0.67, indicating substantial agreement from Landis and Koch’s heuristic [^54].

In order to determine if couple’s preferred playstyles aligned with certain game features, we used the archetype classifications to analyze the outputs of each couple’s MDA activity, described in Section 3.2.3, to determine frequently referenced mechanics, dynamics, and aesthetics for each archetype. This analysis is presented in Section 4.6.4.

## 4\. Findings

### 4.1. Descriptive Overview of Diary Entries

The 13 couples in the study contributed a total of 76 diary entries. Of these, we excluded 5 due to only one partner recording an entry about a specific game session, resulting in a total of 71 entries included for analysis. The open questions on the diary were used to inform the specific questions asked to the couple in the semi-structured interview following completion of the diary entries (see Section 3.2.2), and as such, are not part of the analysis below.

![[game_types_combined.jpeg|Refer to caption]]

Figure 3. How often game types (left) and facets of connectedness (right) were reported in the diary entries.

#### 4.1.1. Games

Participants listed a total of 32 unique games in the entries. By far the most frequently mentioned game, listed in 18.3% of entries, was Stardew Valley. Stardew Valley is designed to be a relaxing, cooperative farming simulator considered to be the archetypical ”cozy game”, characterized by feminist and inclusive design [^88]. Other frequently played games included Splatoon 3 (7%), a cooperative player-versus-environment (PvE) shooting game, and It Takes Two (5.6%), a cooperative action-adventure game following the story of a couple on the verge of divorce.

#### 4.1.2. Connection

We asked participants to report in each session entries how connected they felt to their partner on a Likert scale from 1-5, where 1 was extremely unconnected and 5 was extremely connected. Average connection reported between partners was 4.401/5. Using Pearson’s coefficient, connection reported by each partner in a couple was found to be moderately highly correlated, ($r(69)=0.607,p<0.001$). Together, these results imply that partners felt similarly high levels of connection when gaming together.

#### 4.1.3. Game Types

The diary form asked participants to choose from the following game modalities to describe the game played in their session (Figure 3). The majority of game sessions involved cooperative (85.9%) or goal-oriented (84.5%) games.

#### 4.1.4. Facets of Connectedness

The diary form also asked participants to identify which of Hassenzahl’s six facets of connectedness they felt applied to the game played in their session (Figure 3). Almost all sessions involved games that participants believed to promote awareness (92.9%) or joint action (87.3%).

#### 4.1.5. Time Played

Play sessions lasted for an average of 2.096 hours. The Kruskal-Wallis H test indicated that there was no significant difference in playtime between the game types, but a significant difference in playtime between facets of connectedness, $\chi^{2}(5)=11.23,p=.047$ (Table 2). A possible explanation for this is that games participants listed as promoting expressivity (e.g. Pictionary clones, Scrabble clones) were turn-based competitive games played for a few rounds per gaming session, whereas games listed as promoting physicalness and memories (e.g. Stardew Valley, Minecraft) are more conducive to being played for several hours in a single session.

Table 2. Average playtime reported for entries tagged with each facet of connectedness.

| Strategy | Average time played (hours) |
| --- | --- |
| Awareness | 2.159 |
| Gift Giving | 2.588 |
| Expressivity | 2.091 |
| Joint Action | 2.265 |
| Memories | 2.661 |
| Physicalness | 3.131 |

### 4.2. Why couples value different game modalities

Games that allow for two or more players are normally characterized by dichotomies of cooperative/competitive and interdependent/independent mechanics [^30]. Cooperative games primarily allow (or require) players to complete objectives together within the same game world (e.g., crafting towns and cities together in the building game Minecraft, maintaining a farm together in popular cozy game Stardew Valley, or working together to complete food orders in a high octane kitchen in Overcooked). Competitive games are normally characterized by having players compete against each other, whether 1-on-1 (e.g., chess), a team vs. another team (e.g., Multiplayer Online Battle Arenas like League of Legends), or multiple people vying for the same objective (e.g., Jackbox Games). In our interviews, we investigated how couples viewed cooperative vs. competitive mechanics and how they used them for relational maintenance.

#### 4.2.1. The value of cooperative games

> ”Being able to work together towards the same goal and celebrate our victories together is really great.” - C2B

As long-distance partners are unable to engage in shared tasks [^77] such as chores or errands in person, cooperative games with interdependent mechanics served as a replacement medium for couples to work towards and complete goals together (C3, C5, C7, C8, C9). As C9B explained, “Working towards a goal, especially in games, invites that feeling of fulfillment and accomplishment which can…lead into that feeling of closeness. Because it’s like, hey, we did this, and we did it together. It’s that feeling of being able to accomplish things together \[and see\] our progress together.” Completing these goals together was also accompanied by a sense of shared accomplishment, which was cited as an important reason for enjoying working on joint goals, as “the shared celebration in meeting the goal together brings \[the couple\] closer” (C4B). The presence of a goal was also preferable to some couples, who desired objectives “instead of aimlessly walking around” (C7B).

To accomplish these goals, couples often found themselves communicating to divide labor and complete tasks. Division of labor often occurred along lines of what each partner preferred to do; for example, C10A stated that she prefers to grind and collect items in every game she played with her partner and that this works well for her because she does not enjoy the combat elements that C10B prefers. It was also crucial for in-game tasks that are tedious to complete on one’s own. C2 discussed the collection of resources in farming simulator Stardew Valley, particularly the harvesting of wood from their forest: “Coming in and being like, okay, this is what we want to do, let’s split up the work to make this happen…And that was a lot nicer to together than individual because it’s just so much time.” Indeed, certain game mechanics require partners to rely on each other directly to complete a task. C13 discussed their playthrough of It Takes Two, in which, in certain levels, one partner must shoot nails into the wall in a precise configuration. This allows the other partner to use those nails as platforms that can be climbed up to unlock the next area. This task cannot be completed with just one player, and C13A expressed his appreciation for the game forcing him to rely on his partner: “You actually have this feeling \[that you are\] a couple when you need to work together…you need to really rely on each other. I like this aspect that you are a team.”

More than half of the couples (C3, C5, C6, C7, C8, C11, C12) also discussed how the communication required to accomplish these shared goals also helped their communication skills overall. Often, this was because achieving the objective was difficult, like completing a virtual escape room together (e.g., C5 playing Escape Simulator), determining what they could have done differently when they failed a mission (e.g., C7 playing Astroneer), or needing to put together several parts of the story to understand the full picture (e.g., C8 playing Bokura). However, couples also put their communication to use in different ways; for example, overcoming frustration together. As C3A recalled, “We’ll play a game called Bread and Fred, where it’s like two penguins trying to climb up and it’s sometimes really difficult. And sometimes we just have to keep trying over and over and over again to get over a hurdle. I think in those moments where we do, we are able to not be frustrated at each other, but \[instead\] we’re able to try to achieve a goal together and we achieve it.” C3B also highlighted the importance of positive encouragement in the face of frustrating situations: “I try to encourage her and…she would encourage me. There’s a lot of communication involved in that game, but \[that\] wouldn’t be \[true\] if we were just silent and trying to figure out the game ourselves. You have to really talk a lot. I think \[cooperative\] games encourage us to be more cheerful, playful and talkative.” C12A echoed this sentiment and discussed an instance where she felt guilty for accidentally spending a large portion of their shared bank account in Stardew Valley, but was reassured by C12B that it was okay: “Especially in a low stakes moment, like a game…it’s still nice to get the reassurance, versus in a very high stakes real life moment, where it’s stressful \[and\] it’s hard to take that \[reassurance\] in sometimes. But in the game, I can see that \[reassurance\].”

#### 4.2.2. The value of competitive games

> “I think it’s healthy in relationships to have a little competition every once in a while.” - C10A

Many couples (C1, C2, C3, C4, C6, C8, C11) stated that the primary reason they played games with competitive elements was for the positivity and assurances [^77] that the low stakes competitive environments provided. C4B described the humor she found in losing to her partner: “I take competitive games pretty lightheartedly, so it’s not as if I get upset or anything. I think it’s funny when I die. I think it’s funny when he dies. I think it’s funny when we trade and we both kill each other. It’s a nice playful feeling to have a one-up over him or jokingly having beef with each other.” Even partners who identified as being highly competitive or bad losers stated that they were able to let go of these aspects of their personality when it came to gaming with their significant other. For example, C1B, despite stating, “I’m not a great loser with things in real life. I’m the kind of person who has to win everything”, cited instances in their diary entries where they allowed their partner to win the game for the humor of the situation. C3A reported a similar sentiment: “I’m a competitive person. Maybe it’s petty, but I like to beat him sometimes. But then we get really silly over it and even if we name call each other, it’s all lighthearted, not anything serious.” The reassuring nature of not getting angry or frustrated at each other was discussed within the context of competitive games as well. C4B, who identifies as a woman, expressed that: “It’s also reaffirming as well when you have that kind of dynamic in a competitive environment, because let’s be real, men are scary when it comes to competitive games. But having a time where you play competitive games where neither of you actually get upset at each other for losing \[is\] reaffirming in the dynamic that you share.”

To maintain the positivity that competitive games could engender, most couples maintained that they only chose games where partners were relatively balanced in skill level. For example, C3A and C3B, who primarily play competitive games individually as well as together, discussed only jointly playing games that they were both equally familiar or equally unfamiliar with. C5A, despite never playing competitive games either individually or with C5B, expressed a very similar sentiment: “If we were to play competitive games..it would have to be something that we are like both equally adept \[and\] there would have to be like like some chance involved. So that way, it \[would\] even it out. Say \[C5B\] was incredibly great at something. And I was really bad, or I just had no skill in doing it. I feel like I would not like doing that.”

### 4.3. Liminality between real life and gameplay

> ”Doing a limited time event together is…something we set the time apart specifically to do. In this way I feel like it’s similar to real life, where going to a limited time event together to enjoy something has merits for a relationship building experience, just by having that joint in game time doing something we can’t always take for granted.” - C9A

In the absence of in person time together, couples have found ways to treat certain aspects of the games they play together as parallels to real life shared activities. Some couples (C2, C6, C9) likened their game time to going on a date; for example, when asked as to the value C6 derives from menial in-game tasks such as raids versus the value of open-world exploration, C6B used the analogy, “It’s like doing chores \[together\] versus going on a date.” C9B furthered this analogy, comparing limited-time events in games, which require players to log in and play the game during certain time periods, to visiting an exhibit at a museum: “In person, it would be like, ‘Hey, let’s go to this exhibit together, and walk through that \[together\].’ Whereas digitally, it’s: ‘Hey, there’s this thing that’s up, and we can explore it together.’ And I think that’s a really nice way of interacting.” C9A further elaborated, “The limited aspect makes \[us\] have to set a scheduled time to do it. I think that in itself does add an aspect to it where it does feel more like we would on a date.”

Games also provide couples with “constant opportunit\[ies\] to come up with new silly things” (C9A), primarily inside jokes and topics of conversation that they discuss outside of their time spent playing together. Several couples (C2, C4, C9, C12, C13) referenced inside jokes that they had with each other that bled beyond the boundaries of the game and into their “everyday vocabulary” (C9B). These references surfaced during other activities that the couples engaged in together, such as watching a TV show together (C13), during an in-person activity (C9), or with other friends.

Indeed, almost every couple engaged in joint social interactions with friends [^77]. Since many couples have friends across different countries and time zones, the games and the digital spaces created to play them (e.g., Discord servers) are key ways to stay connected socially. In fact, some couples met and began their relationship in these spaces; for example, “The \[Discord\] server was how I met \[C9B\], because of that \[Minecraft YouTuber\] fan group. It’s been a really nice way to spend time with her, and also other friends with similar interests.” (C9A). Social dynamics in games reflected experiences that partners may have with groups of friends in real life. Positive aspects included spontaneity introduced by the addition of more friends to a play session (C6, C7, C9), or using the game sessions a way “to spend time with people (especially post-COVID)” (C2A). Some couples reflected on the negative aspects of playing with their friends as well; C2B reflected on how playing with friends, as opposed to playing 1:1 with C2A, “takes up a little more of \[her\] social battery”, while C7 discussed how playing with friends who are worse at the game can detract from their enjoyment.

Games were also a way for certain participants to meet their partner’s friends and integrate into existing friend groups, a crucial rite of passage in building a romantic relationship. C6B recounted his experience as the partner being introduced to C6A’s friend group: “It was really nice to get me introduced to some of her friend group, because I didn’t really know these people until we spent three hours running around the open world together, and that was a nice bonding experience. Since I am not as social of a person as \[C6A\], sometimes I need a little bit of an incentive to go out and meet new people.” C11A recalled his opposite experience introducing C11B to his gaming friend group: “\[C11B\] fits in pretty well…I’ve had an ex before who just did not fit into my friend group, so I would never play with both of them at the same time. So this is really nice.”

Couples also stated that the goals of their play sessions 1-on-1 with their partners, as opposed to playing together with friends, were different altogether. As C2A summarized, “I think the focus \[when playing with friends\] is split across multiple people, versus very intentionally spending time with one person.” Indeed, many couples reflected on how playing with friends was mainly a way to “put a little bit of time and energy into that friendship” (C2A), while playing 1-on-1 with a partner was treated as “couple time” (C13A). These sessions were set aside specifically for focusing on their partner and their relationship. Individual sessions also gave partners a chance to be more verbally affectionate and “speak more freely” (C11B), rather than facing “teas\[ing\]…about being disgusting lightheartedly” (C9B).

### 4.4. Expressing affection through game mechanics

> ”Even as they were busy fighting the aliens…\[C13B\] still found time to splash water on me \[to save me\], and I was grateful and felt taken care of for this.” - C13A

While the individual gaming sessions themselves gave couples a safe space to express their verbal affection for their partner, many couples (C1, C2, C3, C4, C9, C10, C12, C13) discussed ways in which they additionally used game mechanics to express more physical feelings of fondness, something which a lack of co-location makes impossible for long-distance couples. C10A recounted her appreciation for C10B secretly crafting a graduation hat for her in Palworld and presenting it to her after she graduated from her masters degree. Similarly, C13A expressed how he felt “taken care of” in the instances that C13B would notice his low health bar before he did himself or when C13B came to his rescue in battles despite being overwhelmed with enemies himself. C2B also discussed the “protectiveness” he felt towards C2A: “I prioritize rescuing \[C2A\]…this \[protectiveness\] is something that you can do in a physical space, but not as much virtually.” Even relatively minor physical actions in the game world, e.g., waiting for a partner’s avatar to catch up while exploring an area (C6, C13), or helping a partner collect resources for their in-game project (C9), helped participants feel closer to their partners. Partners would also “let \[their partner\] win” (C1B), or play games that the other partner specifically enjoyed because it brought them joy to watch their partner enjoy themselves (C4).

Couples also appropriated game mechanics in ways that did not necessarily align with design intentions. Notable examples included C3 playing Spellcast, a game similar to Scrabble, in which they defined the winner as the person who could create the most words related to their inside jokes. When asked to explain this practice, C3A said, “We know we’re making each other laugh…that internally is our highest level that we can achieve.” Defining the heuristic for success as making the other partner laugh was a common practice upon couples to reinforce shared intimacy. In the context of a creative drawing game, in which players must guess what the other person is trying to draw, C1B recalled, “\[In the game\] I genuinely cannot draw anything. Whereas \[C1A\] is very good at drawing. So the \[drawings that C1A makes\] that I can guess are because he can draw well, but the \[drawings that C1B makes\] that he can guess are because he knows me well and I just find that really funny.” Similarly, C13A stated that when playing drawing games with friends, he could always guess which drawings were C13B’s because “\[C13B\]’s sense of humor, or sometimes \[they would draw\] inside jokes, like how I love penguins.”

### 4.5. Framing play with Hassenzahl et al.’s facets of connectedness

> “I guess that’s one of the things about playing games, is that you know they’re doing this to spend time with you. You’re doing something together that does not require you to be like, oh, she’s still there, or is she still interested. Or something that would just quite make you question whether or not they value the current thing that you both are currently doing.” - C7B

Analysis of the diary entries showed that awareness and joint action were the most frequently reported of [^43] ’s facets of connectedness. This was displayed in the qualitative results as well: when asked which facets they found the most important to their play, 10 couples said awareness and 9 said joint action. Participants provided several reasons for the high value placed on awareness, primarily surrounding the “sense of the position or presence of another person” (C3A), even without necessarily actively talking over voice chat. Participants also gave several examples of how game mechanics promoted awareness, such as “passing each other in the game while we’re on our way to different tasks” (C12B), or “doing stupid stuff in the game with our characters, like jumping up and down…that creates that sense of presence” (C3B). As C13A summarized: “I think it’s important for the game to give you a sense that you are playing with your partner live.”

While mechanics promoting awareness in games afford a more passive sense of presence, participants also expressed appreciation for mechanics that promote active presence through joint action. C5A expressed that: “I like joint action \[because\] in order for me to do a task, he has to be here…cause you’re doing the same thing at the same time with each other.” C5A provided It Takes Two as an example of a game with such mechanics (see Section 4.2.1). C9B presented an explicit comparison between joint action and awareness: “Carrying out a joint action almost invites that feeling of closeness more because you’re working towards a goal together rather than just hanging out and vibing.”

When asked about which facets they would like to see implemented more in games, several participants mentioned that they rarely encountered strategies promoting memories; for example, C8A said that “\[they\] were surprised that memories didn’t come up very often in the games \[they\] played”, and C5B expressed that “nothing stuck out to \[them\] as…a game that definitely incorporates that”. A potential reason for this may be that popular gaming platforms execute strategies for memories poorly. For example, C2A mentioned that “the \[Nintendo\] Switch system for sending screenshots to your personal devices really should be better.” C9B expressed a similar problem with the Steam platform: “A lot of people will take screenshots and then they just won’t know where to find them. That happens to me a lot. I’d taken screenshots in \[Don’t Starve\], and they were buried with the Steam folder, and then in the game apps folder, and then in the game folder, and then there’s a screenshot folder. It’s just so hard to find. If more games had a more accessible way of looking at it, I think that would definitely help.” Due to the lack of functional memory saving, several participants expressed that they save special memories manually; for example, C1 and C2 discussed how they screenshot or take pictures of the game screen with their phones to save memories, C4B described “a Discord channel dedicated to quotes and screenshots and special moments”, and C9B described their elaborate system for memory saving: “I have all my screenshots sorted into folders for every individual playthrough, with different co-op modes, with individually modded playthroughs…occasionally when I open it up, I’ll be like, here’s a screenshot of when we built this together.” Indeed, there was an expressed need for better implementations of strategies for memories. As C11A stated, “I think I would like to see more of memories…it would be nice to have cute little screenshots of our characters or places or something that we made together that we can refer back to.”

Physicalness was the least reported facet in the diary entries. When participants discussed it, it was primarily in the context of being able to interact with their partner’s avatar (e.g., “In games like Minecraft, where you’re actually playing as a character interacting in the world…the character is like their own person.” - C9B), or examples of mechanics that translate to physical affection (e.g. “It’s nice to be able to hug \[C5B\] \[in Stardew Valley\] as much as I want…it takes a few seconds and interrupts whatever you’re doing. In real life I’m pretty physically affectionate and so I feel like that aspect of our real relationship is translating.” - C5A). However, in [^43] ’s framework, strategies promoting physicalness revolve around firsthand physical sensation, primarily mediated through haptic experiences. While some console controllers and mobile devices have recently implemented haptic feedback that corresponds with in-game events, these are primarily for single player games. In addition, the majority of desktop games lack the requisite hardware for haptics. These are gaps that are open for further exploration in design and research contexts.

### 4.6. Developing couple play style archetypes

Our analysis yielded three play style archetypes: 1) couples who strictly preferred playing cooperative games that prioritize joint action, 2) couples who play a balanced mix of competitive and cooperative games, and 3) couples that prefer competitive games for the afforded expressivity. These were not archetypes that the research team had preconceived and we did not describe or prompt participants to identify with any of these profiles. While these archetypes and associated facets of connectedness could be applied to any romantic couple gaming together, we found the archetypes to be particularly helpful in brainstorming design prototypes for long-distance couples, presented in Section 5.3.

#### 4.6.1. Archetype 1: Strongly prefers co-op games, strongly prioritizes joint action

A plurality of couples (46%) strongly prefer games with cooperative elements over those with competitive elements, exhibiting a preference for gameplay that promotes collaboration and mutual trust-building. Notably, couples in this archetype tended to explicitly avoid playing competitive games against their partner. This was often due to a perceived imbalance in gaming skill between partners, e.g. C10A: ”I don’t really perform well in competitive games. And \[C10B\] likes competitive games and he is really good at it. That’s why I don’t feel like I’m contributing enough.” C5A echoed this sentiment, stating: ”I’m really bad at competitive stuff. And I’m not one to do things that I’m very bad at. I’m not adventurous in that way.” These sentiments align with previous findings regarding skill differentials in social gaming contexts [^39]. Couples in this archetype tended to prefer games such as Stardew Valley, characterized by its casual, cooperative, and repetitive nature. They tended to highly value awareness and joint action and placed a strong emphasis on teamwork, shared goals and accomplishments, and mutual support. These attributes align strongly with [^91] ’s Relationship motivation, where ”willingness to form meaningful relationships that are supportive in nature” is prioritized. Additionally, their preferred elements from the MDA activity, such as ’having a storyline and background story’ and ’fantasy’ (see Figure 5) indicated a motivation for [^91] ’s Immersion (”enjoy creating avatars with histories that extend and tie in with the stories and lore of the world”).

#### 4.6.2. Archetype 2: Balancing co-op and competitive, prioritizes awareness

Couples who fall under this archetype (38%) are characterized by their preference for cooperative games, although they are not exclusively committed to them, as they balance their preference by occasionally engaging in competitive gaming. Although similar to Archetype 1 in terms of valued facets of connectedness, namely awareness and joint action, couples in this archetype tended to engage in more competitive gameplay together, whether competing on a team in games such as Splatoon 3 or League of Legends, or casually competing against each other in games such as Jackbox. Like Archetype 1, couples in this archetype seem to be motivated by the Relationship aspects of play, but their preferred MDA elements, namely ’missions’, ’mini games’, and ’object collection’ (Figure 5) indicate that they also value Achievement (”accomplishing goals and accumulation of items that confer power”) [^91].

#### 4.6.3. Archetype 3: Strongly prefers competitive, strongly prioritizes expressivity

A minority of couples (16%) displayed a preference for 1v1 gameplay, exemplified by casually competitive trivia games such as Skribbl.io (a Scrabble clone) or drawing games similar to Pictionary. Couples in this archetype stated that they enjoy casual competition and suggest that competitive gaming offers more opportunities for playful jokes, teasing, and banter, which increase overall engagement and enjoyment. These aspects partially align with [^91] ’s Manipulation (”enjoy deceiving, scamming, taunting, and dominating”), albeit with lighthearted intentions. Their preferred MDA elements, namely ’points’, ’increasing difficulty’, and ’receiving rewards’ (Figure 5) also showed a motivation for Achievement. Although both couples in this archetype played cooperative games, they were the only couples to explicitly mention perceived drawbacks of playing cooperative games together. For example, C3A said that she believed that the ”communication aspect \[of cooperative games\] can be emotionally exhausting after a while, especially if you’re \[upset\].” C3B added that he likes being ”bound by his own skill level” and values the autonomy of most competitive games. Indeed, both couples in this archetype consistently listed expressivity as a key design feature in the games they play together.

#### 4.6.4. Connecting Archetypes with MDA Activity

![[x3.jpg|Refer to caption]]

Figure 4. The five raters independently gave each couple a Likert score ranging from 1-5 on two axes: cooperative and competitive. Averaging these ratings for each archetype showed clear divisions between each archetype on these axes.

![[x4.jpg|Refer to caption]]

Figure 5. Commonly used mechanics, dynamics, and aesthetics referenced across archetypes in the MDA activity.

| Couple ID | Archetype | Description of ideal game to play together |
| --- | --- | --- |
| C1 | A3 | ”Like It Takes Two with more 1v1 aspects and the ability to screw the other player over” |
| C2 | A2 | ”Age of Empires with horses to make it less war simulator and more whimsical; Animal Crossing with killing” |
| C3 | A3 | ”SIMS if you could roleplay as seals competing to be the biggest” |
| C4 | A2 | ”Multiplayer Breath of the Wild” |
| C5 | A1 | ”It Takes Two combined with the open world and character creation aspects of Baldur’s Gate, with puzzles like those in The Witness” |
| C6 | A2 | ”Genshin Impact if it was an MMO” |
| C7 | A1 | ”Final Fantasy XIV but more dynamically adjusted so that casual players can still complete a lot of content” |
| C8 | A2 | ”Combination of the mechanics of Wobbly Life and the character and story depth of Bokura” |
| C9 | A1 | ”Combination of the open world aspects of Genshin Impact and the gathering mechanics and limited time activities of Stardew Valley” |
| C10 | A1 | ”Red Dead Redemption with sandbox functionality; Skyrim with more memorable characters and better narrative” |
| C11 | A1 | ”Borderlands if it took place in the world of Apex Legends” |
| C12 | A1 | ”Coffeeshop simulator where one person takes care of all the management and inventory and the other interacts with the NPCs” |
| C13 | A2 | ”It Takes Two but with collectibles or trophies for doing certain tasks (similar to Stardew Valley mechanics)” |

Table 3. Couples’ descriptions of their ideal game to play together, based on their preferred mechanics, dynamics, and aesthetics listed in the MDA activity.

Couples’ preferences in the MDA activity aligned with the developed archetype descriptions (see Figure 5), with A3 primarily choosing features of competitive games (e.g., points, turn taking, rewards for high scores). When asked to describe their preferred games, they expressed a desire for 1v1 gameplay, e.g., C1B expressing that they ”would only want \[the co-designed game\] to be against each other”, C1A valuing ”the ability to mess with the other player”, or C3 describing their ideal game as ”the SIMS but with seals competing to be the biggest.” A1 prioritized exploration and story-based games, e.g., ”Borderlands (a cooperative story game with exploring and level progression) with more relatable characters, or if Apex Legends (a battle royal multiplayer game) had a story mode” (C11). Couples in A2 chose a mix of both cooperative and competitive elements, e.g., C2 describing their ideal game as ”Age of Empires (a real time strategy game where players gather resources to fight opposing factions) but with horses” (see Figure 6). A full list of couples’ descriptions of their ideal games to play together is presented in Table 3.

![[x5.jpg|Refer to caption]]

Figure 6. Design artifact from C2 in Archetype 2 describing their ideal game.

## 5\. Discussion

Our research explored how couples in LDRs value different modalities and mechanics in digital games, and how they use games as a medium through which they can simulate real life activities and express affection to each other. We also developed couple archetypes to represent different values that couples have around their own play.

In the following sections, we discuss implications for HCI researchers and game designers who are seeking to create new technologies for couples in long-distance relationships. As the number of LDRs are believed to be on the rise, this is a crucial period to consider how we, as researchers and designers, can support this lived experience through game design and the creation of game-adjacent applications.

### 5.1. Games as relational maintenance

Our findings build upon [^36] ’s investigation of couples’ exhibited maintenance behaviors in League of Legends, which showed that couples reported high relational quality due to their time spent gaming together. We extend those findings by investigating long-distance couples specifically, and how they engage in relational maintenance in a wider range of games. Indeed, relationship maintenance behaviors are key to the success of long-distance relationships [^27]. Broadly, the couples in our study used games as a shared leisure activity, an important relational maintenance strategy [^17]. Moreover, we found that participants’ in-game behaviors mapped to [^77] ’s typology of relational maintenance strategies. In the positivity dimension, participants generally ”act\[ed\] cheerful and positive” and ”\[tried\] to be romantic, fun, and interesting” with their partners during play. More specifically, participants were ”patient and forgiving of \[their partner\]” (such as C12A’s anecdote about accidentally spending a large portion of C12’s shared Stardew Valley money), and ”attempt\[ed\] to make \[their\] interactions very enjoyable” (such as C1B allowing C1A to win even though it is against their competitive nature, or C3 defining making their partner laugh as the heuristic of success). In the assurances dimension, participants primarily appropriated game mechanics to ”show his/her/their love to \[their partner\]”, such as through C10B’s crafting of a presenet for C10A, C13B risking their in-game safety for C13A, or C9 helping each other with individual in-game projects. In the network dimension, participants ”focused on common friends and affiliations” through joint play sessions with friends, and simultaneously displayed to their partners that they ”like\[d\] to spend time with the same friends”. In the tasks dimension, participants showed their partners that they could ”help equally with tasks that need to be done” and ”share in joint responsibilities” through collaboration in cooperative games, such as the division of labor discussed by C2 and C10. Finally, in the openness dimension, games served as a space for participants to ”tell \[each other\] how they/he/she feels about the relationship” and to effectively enact ”what he/she/they need/want from the relationship” through one on one playtime, as discussed by C2, C11, and C13.

It is important to note the particular role of games for these long-distance couples. The high degree of liminality to real life that games afford is crucial: it serves as a medium through which to engage in a much wider range of relational maintenance behaviors than otherwise available to them. While positivity, assurances, and openness can be expressed through common means of computer-mediated communication such as messaging or calling, it is difficult to engage in network or task behaviors. However, our participants showed how they are filling these gaps through their joint play. Conversely, while co-located couples may also use games as a form of relational maintenance, they have a wider range of options available to them through which to fulfill maintenance behaviors; i.e. in-person dates, social hangouts, or sharing a physical space. Games are one of the only mediums through which long-distance couples can engage in these maintenance behaviors, and therefore merit further exploration in the context of maintaining - and thriving in - long-distance relationships.

### 5.2. Appropriation of games and their mechanics to express affection

[^45] discuss how ”intimate relationships are mediated heavily by the symbolic representations in the game itself”. We extend those findings with practices similar to those described by [^51] and [^60] regarding the ‘appropriation’ or ‘misuse’ of technology to express intimacy and affection, in ways likely not intended by the designers. [^43] describe such practices as: “a product of people’s inventiveness to fulfill their needs even in the face of ’inappropriate’ technological solutions”. Similarly, [^9] describe how players ”adopted usage patterns and ascribed meanings to video games that were not inscribed in their original designs” during difficult circumstances. We witnessed this inscription of meaning through the adjustments that couples made to suit their relationship dynamics, or to embed personal meaning and shared histories into their gaming experiences. Descriptions of joint gameplay also highlighted participants’ deep understanding and recognition of their partner’s likes and preferences. These inventive practices also underscore the importance of mutual recognition and support in relationships in instances where participants would prioritize their partner’s happiness and satisfaction over their own within the game.

It is notable that there are very few popular games designed explicitly for couples, let alone couples in long-distance relationships. Of the games mentioned in our sample, It Takes Two likely comes the closest to meeting these specifications, as it is specifically designed to be played with two people and the two player characters are a couple. Long-distance technologies in general have been thoroughly explored in HCI research, yet few of these findings have been translated to game design. We can draw upon our findings as well as learnings from HCI research to suggest modalities and mechanics that may promote connection between couples in games. For example, the theme of shared inside jokes or secret languages has been explored previously and was found to create a strong feeling of relatedness [^21]. Game designers could implement an object akin to [^38] ’s Cube within games as a collectible, which allows the couple to both engage in the joint action of discovering the object and enabling them to develop their own ”inside” language. Multiplayer features akin to [^49] ’s Hello There exist (e.g., custom scavenger hunts in Minecraft, player generated messages hidden around the world in Elden Ring), but the mechanics could be tuned such that only a specific player would be able to activate a specific object or message, thus allowing partners to hide gifts for each other. In a related vein, just as C10B crafted a graduation hat for C10A to surprise her with, mechanics could be added to generate crafting recipes based on player preferences or real-life events such as birthdays or other celebrations. Drawing upon the joint action strategy, game designers could also consider adding more event-based or limited-time features to simulate the feeling of a ”date” as described by C9, and including special collectibles that represent their shared participation in the event (e.g., matching avatar outfits).

While these examples represent [^43] ’s facets of connectedness as applied to a subset of our findings, designers could use this framework to further surface potential ways in which players appropriate game mechanics in novel ways and use those findings to design game modalities specifically targeted at long-distance couples.

### 5.3. Design Recommendations

#### 5.3.1. Investigating on a per archetype basis

While [^30] suggest that cooperative and inderdependent mechanics in games are more effective in promoting social closeness, the behaviors and preferences expressed by Archetype 3 (competitive, prioritizes expressivity) suggest that more investigation may be warranted regarding how competitive mechanics factor into positive behaviors in close dyadic relationships. Indeed, our findings show that long-distance couples are not monolithic in the ways they play games together, as evidenced by the significant differences in play time and preferred game types between our developed couple archetypes. These differences would also have an effect on designing for/with couples with strong preferences for different modalities of games. This not only includes different game mechanics (see Section 4.6.4 for examples), but extends to interfaces or products designed for different couple archetypes as well. Values around play styles, implicit and explicit motivations [^91] [^63], preferred game mechanics, and tool design for couples in LDRs could be explored through participatory design activities, building on our findings from the MDA activity and archetype classifications.

#### 5.3.2. Addressing gap around ”memories” facet: Prototyping third party application for memory storing

To address the user needs expressed regarding better memory saving functionality for digital games (see Section 4.5), our research group prototyped a desktop overlay (Figure 7) connected to an application in which couples can store screenshots and recordings of their joint play sessions (Figure 8). The goal of such an application would address the lack of standardization between game or platform photo functionalities and provide a single location where users could access shared photos and recordings. Drawing inspiration from other cloud photo services that allow users to save and curate their images, such as Apple iPhotos or Google Photos, the proposed ”digital diary” application would allow couples to organize memories into game-specific journals and allow for minor image editing functionality such as adding text boxes, stickers, or GIFs.

![[x6.jpg|Refer to caption]]

Figure 7. The desktop overlay, shown on the right side of the screen, allows users to easily take screenshots or screen recording from their gameplay. These are then saved into the diary application.

![[x7.jpg|Refer to caption]]

Figure 8. An initial low-fidelity prototype of the ”digital diary” application home screen, developed by our research team.

#### 5.3.3. Addressing gap around ”physicalness” facet: Participatory design work for peripheral design

Although researchers have devised numerous haptic devices to simulate physical intimacy over long distances [^58] [^14] [^89], few of these designs have relied on grounded observations or participatory design. Our findings show that players value “awareness” more than any other of [^43] ’s six facets of connectedness, and simultaneously engage with “physicalness” less than any other facet. Given that researchers have developed numerous hardware peripherals to promote awareness, the low incidence of physicalness in our findings suggests that desktop game makers are underusing haptic technologies. Moreover, accounts of the irreplaceability of ‘physical protection’ (C2B) and the ‘emotional exhaustion’ (C3A) of constant verbal communication during cooperative play reveal opportunities for further research into interpersonal haptics. The diversity of gameplay forms and preferences reported by participants emphasizes the need for participatory design approaches to better tailor haptic technologies to users’ relational needs.

Advances in spatial computing give researchers new opportunities to engage participants in designing haptic technologies to support awareness. Augmented Reality (AR) headsets, like haptics, can provide awareness to users beyond the scope of a computer monitor. For example, a system similar to inPhase [^85] could transmit a flexible set of key gameplay events (e.g., loss of health, acquisition of resources, change in proximity) from one partner’s game to another partner’s AR headset has potential to heighten awareness. Researchers could also utilize other basic haptic or AR devices in participatory design workshops with couples to generate awareness-promoting solutions. For example, couples could brainstorm how they would integrate haptics into specific joint game scenarios (e.g., how to represent their partner’s presence during combat sequences, resource management, or exploration).

## 6\. Limitations

A key limitation of this study is the relatively small number of couples interviewed, and correspondingly, the small number of couples that correspond to the developed archetypes. In addition, there may exist different variations of play dynamics that exist between couples but were not observed in the couples in this study, such as couples that may have a larger difference in their level of interest in playing games (e.g., one partner is more of a reluctant game player than the other), or couples that may interact with games in different ways, such as watching their partner play without playing themselves. Although we did not intend to recruit solely from an American context, our recruitment methods resulted in a primarily American context with few international participants. Different relationship norms exist in different cultures, so future work may explore cultural differences in relationships and gameplay. As we recruited for dyadic couples, these findings do not reflect the experience of people with non-normative relationship dynamics such as polyamory, which have been largely unexplored in HCI and design [^50].

## 7\. Conclusion and Future Work

In this work, we investigated how 13 couples in long-distance relationships are using video games as a strategy for relational maintenance. We used a diary study, semi-structured interviews, and a mechanics-dynamics-aesthetics design activity to probe couples’ values around how they use play to maintain emotional connection over distances often involving multiple time zones and thousands of miles. We observed differences in couple play styles and classified them into archetypes based on these variations. In addition, we build on a long legacy of HCI literature detailing how people appropriate technological affordances to express affection. Building on the design implications developed in this work, future work could involve exploring improved functionalities around facilitating memory making and physicalness in digital games for couples, including participatory design workshops for haptic experiences, co-design between game/platform developers and couples, or creating a system similar to the one we describe in Section 5.3.2. We contribute an empirical understanding of how couples in long-distance relationships are using games to maintain emotional connection, and provide design recommendations for game designers and researchers to create more technologies targeted at this growing population.

###### Acknowledgements.

This work was supported by the University of Washington’s Human Centered Design & Engineering department. The authors would also like to thank the participants for sharing their experiences, and our directed research group for their valuable design insights.

[^2]: Michelle Ahlstrom, Neil R Lundberg, Ramon Zabriskie, Dennis Eggett, and Gordon B Lindsay. 2012. Me, my spouse, and my avatar: The relationship between marital satisfaction and playing massively multiplayer online role-playing games (MMORPGs). *Journal of Leisure Research* 44, 1 (2012), 1–22.

[^3]: Matthew Barr and Alicia Copeland-Stewart. 2022. Playing video games during the COVID-19 pandemic and effects on players’ well-being. *Games and Culture* 17, 1 (2022), 122–139.

[^4]: Jennifer M Belus, Kimberly Z Pentel, Matthew J Cohen, Melanie S Fischer, and Donald H Baucom. 2019. Staying connected: An examination of relationship maintenance behaviors in long-distance relationships. *Marriage & Family Review* 55, 1 (2019), 78–98.

[^5]: Kelly Marie Bergstrom. 2009. *Exploring How Romantic Couples Use MMOs as Part of Their Shared Leisure Time*. Ph. D. Dissertation. University of Calgary.

[^6]: Shari M Blumenstock and Lauren M Papp. 2022. Romantic (versus other) events and momentary affect: Immediate and lagged within-person associations among college students. *Journal of Family Psychology* 36, 1 (2022), 57.

[^7]: G Bodenmann. 2005. *Dyadic coping and its significance for marital functioning*. American Psychological Association, Washington, DC, Chapter 2, 33–49.

[^8]: Tom Boellstorff. 2015. *Coming of age in Second Life: An anthropologist explores the virtually human*. Princeton University Press, Princeton, NJ.

[^9]: Arianna Boldi, Amon Rapp, and Maurizio Tirassa. 2022. Playing during a crisis: The impact of commercial video games on the reconfiguration of people’s life during the COVID-19 pandemic. *Human–Computer Interaction* 39, 5-6 (2022), 338–379.

[^10]: Bradford Booth, Mady Wechsler Segal, D Bruce Bell, James A Martin, Morten G Ender, David E Rohall, and John Nelson. 2007. *What we know about Army families: 2007 update*. Family and Morale, Welfare and Recreation Command, Arlington, VA.

[^11]: Nicholas D Bowman and Ron Tamborini. 2012. Task demand and mood repair: The intervention potential of computer games. *New Media & Society* 14, 8 (2012), 1339–1357.

[^12]: Stacy Branham and Steve Harrison. 2013. *Connecting families: the impact of new communication technologies on domestic life*. Springer, London, England, Chapter Designing for collocated couples, 15–36.

[^13]: Virginia Braun and Victoria Clarke. 2006. Using thematic analysis in psychology. *Qualitative Research in Psychology* 3, 2 (Jan. 2006), 77–101. [https://doi.org/10.1191/1478088706qp063oa](https://doi.org/10.1191/1478088706qp063oa)

[^14]: Scott Brave and Andrew Dahley. 1997. inTouch: a medium for haptic interpersonal communication. In *CHI’97 extended abstracts on human factors in computing systems*. ACM, New York, NY, 363–364.

[^15]: Paris Buttfield-Addison, Jon Manning, and Tim Nugent. 2016. A better recipe for game jams: using the Mechanics Dynamics Aesthetics framework for planning. In *Proceedings of the international conference on game jams, hackathons, and game creation events*. ACM, New York, NY, 30–33.

[^16]: Daniel J. Canary and Laura Stafford. 1992. Relational maintenance strategies and equity in marriage. *Communications Monographs* 59, 3 (Sept. 1992), 243–267. [https://doi.org/10.1080/03637759209376268](https://doi.org/10.1080/03637759209376268)

[^17]: Daniel J. Canary, Laura Stafford, Kimberley S. Hause, and Lisa A. Wallace. 1993. An inductive analysis of relational maintenance strategies: Comparisons among lovers, relatives, friends, and others. *Communication Research Reports* 10, 1 (June 1993), 3–14. [https://doi.org/10.1080/08824099309359913](https://doi.org/10.1080/08824099309359913)

[^18]: Camila Caro and Maša Popovac. 2021. Gaming when things get tough? Examining how emotion regulation and coping self-efficacy influence gaming during difficult life situations. *Games and Culture* 16, 5 (2021), 611–631.

[^19]: Michelle Colder Carras, Antonius J Van Rooij, Dike Van de Mheen, Rashelle Musci, Qian-Li Xue, and Tamar Mendelson. 2017. Video gaming in a hyperconnected world: A cross-sectional study of heavy gaming, problematic gaming symptoms, and online socializing in adolescents. *Computers in human behavior* 68 (2017), 472–479.

[^20]: Angela Chang, Ben Resner, Brad Koerner, XingChen Wang, and Hiroshi Ishii. 2001. LumiTouch: an emotional communication device. In *CHI’01 extended abstracts on Human factors in computing systems*. ACM, New York, NY, 313–314.

[^21]: David Cheal. 1987. ‘Showing them you love them”: gift giving and the dialectic of intimacy. *The Sociological Review* 35, 1 (1987), 150–169.

[^22]: Amber Choo, Mehdi Karamnejad, and Aaron May. 2013. Maintaining long distance togetherness Synchronous communication with Minecraft and Skype. In *2013 IEEE International Games Innovation Conference (IGIC)*. IEEE, Piscataway, NJ, 27–35. [https://doi.org/10.1109/IGIC.2013.6659138](https://doi.org/10.1109/IGIC.2013.6659138)

[^23]: Hyemin Chung, Chia-Hsun Jackie Lee, and Ted Selker. 2006. Lover’s cups: drinking interfaces as new communication channels. In *CHI’06 extended abstracts on Human factors in computing systems*. ACM, New York, NY, 375–380.

[^24]: Helena Cole and Mark D Griffiths. 2007. Social interactions in massively multiplayer online role-playing gamers. *Cyberpsychology & behavior* 10, 4 (2007), 575–583.

[^25]: Emily Collins and Anna L Cox. 2014. Switch on to games: Can digital games aid post-work recovery? *International Journal of Human-Computer Studies* 72, 8-9 (2014), 654–662.

[^26]: Sarah M. Coyne, Dean Busby, Brad J. Bushman, Douglas A. Gentile, Robert Ridge, and Laura Stockdale. 2012. Gaming in the Game of Love: Effects of Video Games on Conflict in Couples. *Family Relations* 61, 3 (2012), 388–396. [https://doi.org/10.1111/j.1741-3729.2012.00712.x](https://doi.org/10.1111/j.1741-3729.2012.00712.x)

[^27]: Marianne Dainton and Brooks Aylor. 2001. A relational uncertainty analysis of jealousy, trust, and maintenance in long-distance versus geographically close relationships. *Communication Quarterly* 49, 2 (2001), 172–188.

[^28]: Marianne Dainton and Brooks Aylor. 2002. Patterns of communication channel use in the maintenance of long‐distance relationships. *Communication Research Reports* 19, 2 (March 2002), 118–129. [https://doi.org/10.1080/08824090209384839](https://doi.org/10.1080/08824090209384839)

[^29]: Emma Dargie, Karen L. Blair, Corrie Goldfinger, and Caroline F. Pukall. 2015. Go Long! Predictors of Positive Relationship Outcomes in Long-Distance Dating Relationships. *Journal of Sex & Marital Therapy* 41, 2 (March 2015), 181–202. [https://doi.org/10.1080/0092623X.2013.864367](https://doi.org/10.1080/0092623X.2013.864367)

[^30]: Ansgar E Depping and Regan L Mandryk. 2017. Cooperation and interdependence: How multiplayer games increase social closeness. In *Proceedings of the Annual Symposium on computer-human interaction in play*. ACM, New York, NY, 449–461.

[^31]: developer. 2023. Video Games Remain America’s Favorite Pastime With More Than 212 Million Americans Playing Regularly. [https://www.theesa.com/video-games-remain-americas-favorite-pastime-with-more-than-212-million-americans-playing-regularly/](https://www.theesa.com/video-games-remain-americas-favorite-pastime-with-more-than-212-million-americans-playing-regularly/)

[^32]: Kathryn Dindia. 2003. Definitions and perspectives on relational maintenance communication. In *Maintaining relationships through communication*. Routledge, Oxfordshire, England, 1–28.

[^33]: Steve N Du Bois, Tamara G Sher, Karolina Grotkowski, Talia Aizenman, Noel Slesinger, and Mariana Cohen. 2016. Going the distance: Health in long-distance versus proximal relationships. *The Family Journal* 24, 1 (2016), 5–14.

[^34]: Steve Duck. 1999. *Relating to others 2/e*. McGraw-Hill Education (UK), London, England.

[^35]: Allison L Eden, Benjamin K Johnson, Leonard Reinecke, and Sara M Grady. 2020. Media for coping during COVID-19 social distancing: Stress, anxiety, and psychological well-being. *Frontiers in psychology* 11 (2020), 577639.

[^36]: Sarah Evans, Elizabeth Craig, and Nicholas Taylor. 2018. *Couples Who Slay Together, Stay Together: Benefits, Challenges, and Relational Quality among Romantic Couples Who Game* (1 ed.). Cambridge University Press, Cambridge, England, 80–100. [https://doi.org/10.1017/9781316422823.005](https://doi.org/10.1017/9781316422823.005)

[^37]: Sophie Gaetan, Vincent Bréjard, and Agnès Bonnet. 2016. Video games in adolescence and emotional functioning: Emotion regulation, emotion intensity, emotion expression, and alexithymia. *Computers in Human Behavior* 61 (2016), 344–349.

[^38]: Kasper Garnæs, Olga Grünberger, Jesper Kjeldskov, and Mikael B. Skov. 2007. Designing technologies for presence-in-absence: illustrating the Cube and the Picture Frame. *Personal and Ubiquitous Computing* 11, 5 (June 2007), 403–408. [https://doi.org/10.1007/s00779-006-0072-9](https://doi.org/10.1007/s00779-006-0072-9)

[^39]: Kathrin Maria Gerling, Matthew Miller, Regan L Mandryk, Max Valentin Birk, and Jan David Smeddinck. 2014. Effects of balancing for physical abilities on player performance, experience and self-esteem in exergames. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*. ACM, New York, NY, 2201–2210.

[^40]: Gregory T. Guldner. 1996. Long-distance romantic relationships: Prevalence and separation-related symptoms in college students. *Journal of College Student Development* 37, 3 (1996), 289–296.

[^41]: Adam J Hampton, Jessica Rawlings, Stanislav Treger, and Susan Sprecher. 2017. Channels of computer-mediated communication and satisfaction in long-distance relationships. *Interpersona: An International Journal on Personal Relationships* 11, 2 (2017), 171–187.

[^42]: John Harris, Mark Hancock, and Stacey D Scott. 2016. Leveraging asymmetries in multiplayer games: Investigating design elements of interdependent play. In *Proceedings of the 2016 Annual Symposium on computer-human interaction in play*. ACM, New York, NY, 350–361.

[^43]: Marc Hassenzahl, Stephanie Heidecker, Kai Eckoldt, Sarah Diefenbach, and Uwe Hillmann. 2012. All You Need is Love: Current Strategies of Mediating Intimate Relationships through Technology. *ACM Transactions on Computer-Human Interaction* 19, 4 (Dec. 2012), 1–19. [https://doi.org/10.1145/2395131.2395137](https://doi.org/10.1145/2395131.2395137)

[^44]: Robin Hunicke, Marc LeBlanc, and Robert Zubek. 2004. MDA: A Formal Approach to Game Design and Game Research. *Proceedings of the AAAI Workshop on Challenges in Game AI* 4 (2004), 1722–1726.

[^45]: Kim-Phong Huynh, Si-Wei Lim, and Marko M. Skoric. 2013. Stepping out of the Magic Circle: Regulation of Play/Life Boundary in MMO-Mediated Romantic Relationship. *Journal of Computer-Mediated Communication* 18, 3 (April 2013), 251–264. [https://doi.org/10.1111/jcc4.12011](https://doi.org/10.1111/jcc4.12011)

[^46]: Ioanna Iacovides and Elisa D Mekler. 2019. The role of gaming during difficult life experiences. In *Proceedings of the 2019 CHI conference on human factors in computing systems*. ACM, New York, NY, 1–12.

[^47]: Amy Janan Johnson, Michel M Haigh, Jennifer AH Becker, Elizabeth A Craig, and Shelley Wigley. 2008. College students’ use of relational management strategies in email in long-distance and geographically close relationships. *Journal of Computer-mediated communication* 13, 2 (2008), 381–404.

[^48]: Joseph’Jofish’ Kaye, Mariah K Levitt, Jeffrey Nevins, Jessica Golden, and Vanessa Schmidt. 2005. Communicating intimacy one bit at a time. In *CHI’05 extended abstracts on Human factors in computing systems*. ACM, New York, NY, 1529–1532.

[^49]: Simon King and Jodi Forlizzi. 2007. Slow messaging: intimate communication for couples living at a distance. In *Proceedings of the 2007 conference on Designing pleasurable products and interfaces*. ACM, New York, NY, 451–454.

[^50]: Brian Kinnee. 2024. Designing with Polyamory. In *Companion Publication of the 2024 ACM Designing Interactive Systems Conference*. ACM, New York, NY, 67–69.

[^51]: Martin Knobel, Marc Hassenzahl, Melanie Lamara, Tobias Sattler, Josef Schumann, Kai Eckoldt, and Andreas Butz. 2012. Clique Trip: feeling related in different cars. In *Proceedings of the Designing Interactive Systems Conference*. ACM, Newcastle Upon Tyne United Kingdom, 29–37. [https://doi.org/10.1145/2317956.2317963](https://doi.org/10.1145/2317956.2317963)

[^52]: Mehmet Kosa and Ahmet Uysal. 2020. *Game User Experience and Player-Centered Design*. Springer, Berlin, Germany, Chapter Four pillars of healthy escapism in games: Emotion regulation, mood management, coping, and recovery, 63–76.

[^53]: Gede Putra Kusuma, Evan Kristia Wigati, Yesun Utomo, and Louis Khrisna Putera Suryapranata. 2018. Analysis of Gamification Models in Education Using MDA Framework. *Procedia Computer Science* 135 (Jan. 2018), 385–392. [https://doi.org/10.1016/j.procs.2018.08.187](https://doi.org/10.1016/j.procs.2018.08.187)

[^54]: J. Richard Landis and Gary G. Koch. 1977. The Measurement of Observer Agreement for Categorical Data. *Biometrics* 33, 1 (1977), 159–174. [https://doi.org/10.2307/2529310](https://doi.org/10.2307/2529310)

[^55]: Andrew M. Ledbetter and Jeffrey H. Kuznekoff. 2012. More Than a Game: Friendship Relational Maintenance and Attitudes Toward Xbox LIVE Communication. *Communication Research* 39, 2 (April 2012), 269–290. [https://doi.org/10.1177/0093650210397042](https://doi.org/10.1177/0093650210397042)

[^56]: Katheryn C Maguire and Terry A Kinney. 2010. When distance is problematic: Communication, coping, and relational satisfaction in female college students’ long-distance dating relationships. *Journal of Applied Communication Research* 38, 1 (2010), 27–46.

[^57]: Sahar Mirhadi, Ioanna Iacovides, and Alena Denisova. 2024. Playing Through Tough Times: Exploring the Relationship between Game Aspects and Coping Strategies during Difficult Life Challenges. *Proceedings of the ACM on Human-Computer Interaction* 8, CHI PLAY (2024), 1–25.

[^58]: Florian “Floyd” Mueller, Frank Vetere, Martin R. Gibbs, Jesper Kjeldskov, Sonja Pedell, and Steve Howard. 2005. Hug over a distance. In *CHI ’05 Extended Abstracts on Human Factors in Computing Systems* *(CHI EA ’05)*. Association for Computing Machinery, New York, NY, USA, 1673–1676. [https://doi.org/10.1145/1056808.1056994](https://doi.org/10.1145/1056808.1056994)

[^59]: Daniel Muriel and Garry Crawford. 2018. *Video games as culture: Considering the role and importance of video games in contemporary society*. Routledge, London, England, UK.

[^60]: Carman Neustaedter and Saul Greenberg. 2012. Intimacy in long-distance relationships over video chat. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems* *(CHI ’12)*. Association for Computing Machinery, New York, NY, USA, 753–762. [https://doi.org/10.1145/2207676.2207785](https://doi.org/10.1145/2207676.2207785)

[^61]: Katy E Pearce, Jason C Yip, Jin Ha Lee, Jesse J Martinez, Travis W Windleharth, Arpita Bhattacharya, and Qisheng Li. 2022. Families playing animal crossing together: coping with video games during the COVID-19 pandemic. *Games and Culture* 17, 5 (2022), 773–794.

[^62]: M. Carole Pistole, Amber Roberts, and Marion L. Chapman. 2010. Attachment, relationship maintenance, and stress in long distance and geographically close romantic relationships. *Journal of Social and Personal Relationships* 27, 4 (June 2010), 535–552. [https://doi.org/10.1177/0265407510363427](https://doi.org/10.1177/0265407510363427)

[^63]: Susanne Poeller, Max V Birk, Nicola Baumann, and Regan L Mandryk. 2018. Let me be implicit: Using motive disposition theory to predict and explain behaviour in digital games. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems*. ACM, New York, NY, 1–15.

[^64]: Xiaoke Pu, Ruoxin You, and Wei Huang. 2024. Ourhotel: A Two-Player Cooperative Game Designed for Young Couples in Long-Distance Relationships. In *International Conference on Human-Computer Interaction*. Springer, Berlin, Germany, 348–358.

[^65]: Kelly Quinn and Zizi Papacharissi. 2017. *The SAGE Handbook of Social Media*. SAGE Publications. Londres, New York, NY, Chapter Our Networked selves: Personal connection and relational maintenance in social media use, 353–371.

[^66]: Leonard Reinecke. 2009. Games and recovery: The use of video and computer games to recuperate from stress and strain. *Journal of media psychology* 21, 3 (2009), 126–142.

[^67]: Angel R Rhodes. 2002. Long-distance relationships in dual-career commuter couples: A review of counseling issues. *The Family Journal* 10, 4 (2002), 398–404.

[^68]: Diana Rieger, Lena Frischlich, Tim Wulf, Gary Bente, and Julia Kneer. 2015. Eating ghosts: The underlying mechanisms of mood repair via interactive and noninteractive media. *Psychology of Popular Media Culture* 4, 2 (2015), 138.

[^69]: John Rieman. 1993. The diary study: a workplace-oriented research tool to guide laboratory efforts. In *Proceedings of the INTERACT’93 and CHI’93 conference on Human factors in computing systems*. ACM, New York, NY, 321–326.

[^70]: Erin M Sahlstein. 2006. Making plans: Praxis strategies for negotiating uncertainty–certainty in long-distance relationships. *Western Journal of Communication* 70, 2 (2006), 147–165.

[^71]: Diane J Schiano, Bonnie Nardi, Thomas Debeauvais, Nicolas Ducheneaut, and Nicholas Yee. 2014. The “lonely gamer” revisited. *Entertainment Computing* 5, 1 (2014), 65–70.

[^72]: Raymond Scupin. 1997. The KJ method: A technique for analyzing data derived from Japanese ethnology. *Human organization* 56, 2 (1997), 233–237.

[^73]: Shmuel Shulman and Jennifer Connolly. 2013. The challenge of romantic relationships in emerging adulthood: Reconceptualization of the field. *Emerging Adulthood* 1, 1 (2013), 27–39.

[^74]: Robert J Sidelinger, Gus Ayash, Alexandria Godorhazy, and David Tibbles. 2008. Couples go online: Relational maintenance behaviors and relational characteristics use in dating relationships. *Human communication* 11, 3 (2008), 333–348.

[^75]: Victoria Schwanda Sosik and Natalya N Bazarova. 2014. Relational maintenance on social network sites: How Facebook communication predicts relational escalation. *Computers in Human Behavior* 35 (2014), 124–131.

[^76]: Laura Stafford. 2004. *Maintaining long-distance and cross-residential relationships*. Routledge, Oxfordshire, England, UK.

[^77]: Laura Stafford and Daniel J Canary. 1991. Maintenance strategies and romantic relationship type, gender and relational characteristics. *Journal of Social and Personal relationships* 8, 2 (1991), 217–242.

[^78]: Laura Stafford, Marianne Dainton, and Stephen Haas. 2000. Measuring routine and strategic relational maintenance: Scale revision, sex versus gender roles, and the prediction of relational characteristics. *Communication Monographs* 67, 3 (Sept. 2000), 306–323. [https://doi.org/10.1080/03637750009376512](https://doi.org/10.1080/03637750009376512)

[^79]: Constance A Steinkuehler and Dmitri Williams. 2006. Where everybody knows your (screen) name: Online games as “third places”. *Journal of computer-mediated communication* 11, 4 (2006), 885–909.

[^80]: Rob Strong, Bill Gaver, et al. 1996. Feather, scent and shaker: supporting simple intimacy. In *Proceedings of CSCW*, Vol. 96. ACM, New York, NY, 29–30.

[^81]: Steven L Thorne. 2008. *Computer-mediated communication*. Vol. 4. Springer, New York, NY, C336.

[^82]: Stephanie Tong, Joseph B Walther, et al. 2011. Relational maintenance and CMC. *Computer-mediated communication in personal relationships* 53, 9 (2011), 1689–1699.

[^83]: Sabine Trepte, Leonard Reinecke, and Keno Juechems. 2012. The social side of gaming: How playing online computer games creates online and offline social support. *Computers in Human behavior* 28, 3 (2012), 832–839.

[^84]: Penny Trieu and Nancy K Baym. 2020. Private responses for public sharing: understanding self-presentation and relational maintenance via stories in social media. In *Proceedings of the 2020 CHI conference on human factors in computing systems*. ACM, New York, NY, 1–13.

[^85]: Hitomi Tsujita, Koji Tsukada, and Siio Itiro. 2010. InPhase: evaluation of a communication system focused on” happy coincidences” of daily behaviors. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*. ACM, New York, NY, 2481–2490.

[^86]: Selen Türkay, Allan Lin, Daniel Johnson, and Jessica Formosa. 2023. Self-determination theory approach to understanding the impact of videogames on wellbeing during COVID-19 restrictions. *Behaviour & Information Technology* 42, 11 (2023), 1720–1739.

[^87]: Herbert Wanga, Thobius Joseph, and Mauna Belius Chuma. 2020. Social distancing: Role of smartphone during coronavirus (COVID-19) pandemic era. *International Journal of Computer Science and Mobile Computing* 9, 5 (2020), 181–188.

[^88]: Agata Waszkiewicz and Martyna Bakun. 2020. Towards the aesthetics of cozy video games. *Journal of Gaming & Virtual Worlds* 12, 3 (2020), 225–240.

[^89]: Julia Werner, Reto Wettach, and Eva Hornecker. 2008. United-pulse: feeling your partner’s pulse. In *Proceedings of the 10th international conference on Human computer interaction with mobile devices and services*. ACM, New York, NY, 535–538.

[^90]: Dmitri Williams, Nicolas Ducheneaut, Li Xiong, Yuanyuan Zhang, Nick Yee, and Eric Nickell. 2006. From tree house to barracks: The social life of guilds in World of Warcraft. *Games and culture* 1, 4 (2006), 338–361.

[^91]: Nick Yee. 2006. The demographics, motivations, and derived experiences of users of massively multi-user online graphical environments. *Presence: Teleoperators and virtual environments* 15, 3 (2006), 309–329.

[^92]: Guo Zhang and Susan C Herring. 2013. In-game marriage and computer-mediated collaboration: An exploratory study of Audition. *AoIR* IR14 (2013), 1–6.