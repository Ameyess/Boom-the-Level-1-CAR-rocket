---
title: "Boom Boom - L1 Rocket"
author: "your-name"
description: "Building and certifying an L1 high-power rocket called Boom Boom, including CAD, simulations, avionics, and launch prep."
created_at: "2026-04-05"
---

# April 5: Worked on the initial design of the rocket

Made good progress on the L1 rocket project today. Got the rough CAD model built out in OpenRocket with all the main components sorted out: nose cone, body tube, trapezoidal fins, parachute, shock cord, and engine block. Also ran the motor simulations with the HP-H195NT-10, and the numbers are looking good. Projected apogee is around 1,482 m, max velocity of 471 m/s (Mach 1.389), and stability margin is at 1.8 cal, which is right where it should be for a L1 rocket. Additionally, the recovery deployment looks clean at apogee. I'm happy with how the development is going, and the next step will be refining the CAD and ordering parts.

![OpenRocket simulation](https://stasis.hackclub-assets.com/images/1775351929076-qvdnq1.png)

![OpenRocket simulation 2](https://stasis.hackclub-assets.com/images/1775351992789-42fk6q.png)

![OpenRocket simulation 3](https://stasis.hackclub-assets.com/images/1775352009674-fvvsb0.png)

**Total time spent: 2 hours**

# April 6: Worked on refining the L1 Rocket and researching parts

Today I looked at some example L1 rockets and found that the motor requires a retaining ring. This ring holds the motor in place during launch and prevents it from ejecting out of the rocket. I also came across a few ways to 3D print this part instead of buying it, which I might do since it's the cheaper option.

I also spent time working on my Onshape document and adding components. One of the bigger frustrations today was trying to track down a 3D model of the motor I want to use (H135W-14A). There just aren't any available online, so I had to move on from that for now.

From there, I shifted focus toward designing a payload bay that can sit inside the nosecone and house an altimeter and GPS unit. I put together a rough model of the frame. The top two compartments will hold the altimeter and GPS equipment, and the middle sections will hold a battery or whatever other payload ends up being needed.

Overall, today was mainly design work again, but more focused on refining exactly what the rocket needs to include. Next session, I'm aiming to get the motor added into the CAD and update the masses in OpenRocket.

![Payload bay CAD](https://stasis.hackclub-assets.com/images/1775516731066-yyxc59.png)

![Payload bay CAD 2](https://stasis.hackclub-assets.com/images/1775516733549-lq5zj5.png)

**Total time spent: 1 hour**

# April 7: Worked on adding more details to the CAD and researching parts

Today I worked on the payload portion of Boom, the L1 rocket. This session was a mix of both CAD and research for various components and parts of the rocket. However, there are still uncertainties to solve.

On the research side, I landed on a GPS solution: the Pocket-GPS design using a GPS Neo-6M module paired with an ESP32. This should allow for a cheap and reliable GPS solution. It can display altitude, latitude, longitude, speed, and satellite count, which covers everything needed to track the rocket. I need to research how to send the information back to a server to track the rocket's position.

I also started sizing out the payload bay compartments around these components and looked into mounting and fastener options for securing everything inside the bay. The main roadblock was the uncertainty around specific dimensions and specs of the fasteners and parts. Without the exact measurements of the GPS modules, most of the modeling still feels like an estimate until those numbers are confirmed.

Next session, I will confirm the physical specs of the GPS and ESP32 modules and get them properly modeled into the CAD.

![CAD payload bay](https://stasis.hackclub-assets.com/images/1775589056411-u80xar.png)

![CAD payload bay 2](https://stasis.hackclub-assets.com/images/1775589078229-ke28qy.png)

![CAD payload bay 3](https://stasis.hackclub-assets.com/images/1775589091319-eob6qq.png)

![CAD payload bay 4](https://stasis.hackclub-assets.com/images/1775589435167-g2a611.png)

**Total time spent: 1.5 hours**

# April 8: Worked on CAD and Research

Today I continued working on the payload section of Boom, though this session ended up being more of a research detour than I had planned. Coming off of last journal, I had originally planned to confirm the physical specs of the GPS and ESP32 modules and get them properly modeled into the CAD, but that didn't happen.

Once I started pricing everything out, I realized the module would have cost way too much. The GPS Neo-6M and ESP32 combo seemed like a solid, cheap solution, but dedicated altimeter modules on top of that pushed the cost too high.

Instead of sticking with the ESP32 route, I started looking at alternatives. One strong option is a simple Arduino Nano paired with a BMP280 barometric pressure sensor, which reads altitude by detecting changes in atmospheric pressure. This has been proven by many other DIY rockets. The whole setup should cost around $20 USD, which wouldn't push the budget too far. This will cover altitude; however, I still need to figure out the GPS portion and how to log the data.

On the other side of the session, I shifted over to CAD and started working on the motor geometry. I found the official motor assembly drawing, which gave me the key dimensions I needed. Using that as a reference, I was able to model it out in CAD and create a rough outline of what the rocket engine might look like. I still want to double-check with real images and blueprints what the exact dimensions of the rocket motor are.

Next session, I want to compare the Arduino Nano and BMP280 option, look into any affordable GPS modules that are worth considering, as well as continuing the CAD now that the motor geometry is in a good place.

![Motor CAD](https://stasis.hackclub-assets.com/images/1775653298319-0485jj.png)

![Motor CAD 2](https://stasis.hackclub-assets.com/images/1775654368092-sjhjpc.png)

![Motor CAD 3](https://stasis.hackclub-assets.com/images/1775652514886-e82cog.png)

![Motor CAD 4](https://stasis.hackclub-assets.com/images/1775654053613-pmx9ey.png)

**Total time spent: 2 hours**

# April 9: Worked on MORE CAD, Avionics, and shtuff :)

Today I continued working on Boom, and just like last session, I ran into a few problems.

Today's goal was to compare the Arduino Nano and BMP280 option, look into affordable GPS modules, and keep adding detail to the CAD. The CAD part happened, but the electronics took a turn for the worse.

I realized the Arduino Nano and BMP280 combo I had been considering doesn't actually work out. So I went back to square one on the avionics side and started looking at what other DIY and L1 rocketeers are actually using. Two options stood out to me the most: the Eggtimer ION and the PerfectFlight Firefly. The Firefly is cheaper, but it won't give me as much data as the Eggtimer.

I also did a check for the L1 requirements. Parachute recovery is mandatory for good certification because I have already incorporated a parachute into Boom. However, I still need to find out the right ejection charge delay so the parachute opens at or after apogee.

On the CAD side, I got the motor geometry dialled in, and the engine now fits properly within the airframe. The assembly is starting to look like an actual rocket. I also added the rail lugs and the centering rings for the motor.

Next session: make a final call on the altimeter — ION vs. Firefly.

![CAD assembly](https://stasis.hackclub-assets.com/images/1775771408626-p774xy.png)

![CAD assembly 2](https://stasis.hackclub-assets.com/images/1775766862071-91of3f.png)

![CAD assembly 3](https://stasis.hackclub-assets.com/images/1775766875120-gckhzx.png)

![CAD assembly 4](https://stasis.hackclub-assets.com/images/1775771376869-2crjcb.png)

![CAD assembly 5](https://stasis.hackclub-assets.com/images/1775771384794-fzgiu2.png)

**Total time spent: 2 hours**

# April 10: Worked on avionics and CAD

Today I continued working on Boom and decided on the altimeter debate from last session. The goal of this session was to finalize the altimeter module and then add and modify the CAD to accommodate it.

I went with the PerfectFlight Firefly over the Eggtimer ION. The lower cost and smaller form factor are better for an L1 flight. Additionally, it is better to keep the L1 flight simple, so fewer things can go wrong. The Firefly handles apogee detection and ejection charge deployment, which is everything I need for a certification flight.

On the CAD side, I designed a small compartment for the payload bay to house the Firefly. It sits within the nose cone shoulder and will be glued to hold it in.

Overall, this session was pretty good. I finalized the altimeter, and the next session will be focusing on finalizing the CAD and submitting the design for review.

![Firefly compartment CAD](https://stasis.hackclub-assets.com/images/1775846864774-xfvpg8.png)

![Firefly compartment CAD 2](https://stasis.hackclub-assets.com/images/1775846892743-yw7a7j.png)

**Total time spent: 1 hour**

# April 12 (2 AM): Worked on CAD

Today's session on Boom was a CAD-focused one. The main tasks were tidying up the existing components, chamfering the edges of the fins, and assigning materials and weights to the parts. It is important to get these items filled out before running simulations, as mass and aerodynamics do play a role in the overall performance of the rocket. I also modeled a few miscellaneous bits and pieces that hadn't been addressed yet, such as the eye bolts. I also added the pilot holes for the altimeter.

Today's session went on without a hassle and was smooth. Next session should be the final push to wrap up the CAD and get the design ready for review.

![CAD fin detail](https://stasis.hackclub-assets.com/images/1775961521337-rrh1gb.png)

![CAD assembly](https://stasis.hackclub-assets.com/images/1775961069785-xi5ooz.png)

![CAD fin chamfer](https://stasis.hackclub-assets.com/images/1775961006138-ugcw6l.png)

**Total time spent: 0.5 hours**

# April 12 (10 AM): Final touches

Today I worked on the final touches for Boom. There was not much to CAD or research, so I spent some time exploring possible decals and logos for the rocket. Apart from that, I also worked on some miscellaneous things, such as fixing the assembly and addressing other minor issues.

Overall, I am happy with how the design turned out, and I think it will fly great and hopefully reach the speeds I am aiming for. I also sliced the nose cone and fins, so they are ready to print. For the fins, I created a technical drawing so they can be sent to the CNC machine at my robotics team.

I really like this logo, as it is minimalistic yet detailed enough to look great. I think the rocket would look awesome flying with it.

![Rocket decal](https://stasis.hackclub-assets.com/images/1776047640300-nw635x.png)

![Logo option 1](https://stasis.hackclub-assets.com/images/1775990074637-m7ui1q.png)

![Logo option 2](https://stasis.hackclub-assets.com/images/1775989898891-2orets.png)

**Total time spent: 0.5 hours**

# May 3: Final touches Mk2

In this session, I worked on updating the model to incorporate the feedback from the review. I went through each point raised and worked on getting the necessary updates done. I also uploaded the BOM as a CSV file to GitHub, which had been flagged as missing.

I also took the time to talk with several experienced L1 rocket flyers to get some real-world answers to the review concerns. For the question of how the rocket will be controlled and guided, they explained that with a properly stable rocket, the thrust pushes downward and the rocket moves in the opposite direction thanks to Newton's Third Law. On top of this, the rocket will also be guided on a launch rail during ignition to keep it upright while the motor gets up to speed.

For the visibility side of it, many people recommended making the rocket a very bright colour so it stays visible to the naked eye as it descends, as a tracker is way out of the budget, as shown in previous journals.

![Review feedback](https://stasis.hackclub-assets.com/images/1777842665016-jdf862.png)

**Total time spent: 1 hour**

# May 7: Final touches Mk3

## Questions to Answer

**a)** If you can't do trajectory control, how are you going to make sure it's not going anywhere it's not supposed to be?

**b)** How will the Firefly be retrieved if you don't know where it is?

**c)** How are you going to make sure the thing isn't going to go down barrelling at terminal velocity and destroying itself?

## Responses

**A)** For the question of how the rocket will be controlled and kept on course without trajectory control, the answer comes down to stability and launch setup. As stated in a previous journal, in a properly stable rocket, the thrust pushes downward, and the rocket moves in the opposite direction. This might raise concerns because even the most stable rockets do drift and can change direction, which is why I included fins in my rocket design. The fins will help the rocket stay in the air while maintaining its stability. Additionally, RocketPy simulations accurately show where the rocket will end up.

![RocketPy simulation — red line is the rocket flight path](https://stasis.hackclub-assets.com/images/1778195888041-m5yur2.png)

**B)** In addition to simulating and predicting where the rocket will land, we will paint it a bright colour so it remains visible to the naked eye as it descends.

**C)** For the concern about the rocket coming down at terminal velocity and destroying itself, this is handled through the recovery system. The rocket will have a parachute already listed in the parts list, along with an ejection charge built into the motor itself. When the motor burns out, the charge fires automatically, and users can adjust the time by using the provided tool in the rocket motor package, as well as an alternative tool which I already own.

## Use of the Firefly

The onboard Firefly computer will only be used to track altitude during the launch. The Firefly does not have a GPS, a way to detach the chute, or any other function within the rocket. Since the Firefly acts as its own module, I could not find/make a wiring diagram for it.

I hope these answers clarify where Boom Boom is heading, and I hope now you guys can see my vision. :)

**Total time spent: 1 hour**

# May 12: Final touches Mk4

In today's session (final session before build, hopefully), I worked on the reviewers' feedback.

![Reviewer feedback](https://stasis.hackclub-assets.com/images/1778621315843-hz265c.png)

## Point 1 — GitHub Organizing

The first part of the feedback that caught my eye was the horrendous-looking GitHub; I 100% agree that it should be organized into folders. In this session, I did just that: I organized the GitHub into folders for CAD, Simulations, and the Firefly payload altimeter module.

The CAD folder houses the CAD for BoomBoom.

![CAD folder](https://stasis.hackclub-assets.com/images/1778622202178-og81d0.png)

The Simulation folder holds the various simulations I did on trajectory and stability.

![Simulations folder](https://stasis.hackclub-assets.com/images/1778622269304-lfabou.png)

The Firefly folder holds the manual for my altimeter module as well as the wiring diagram for it.

![Firefly folder](https://stasis.hackclub-assets.com/images/1778622308460-0kyg9x.png)

![Firefly folder 2](https://stasis.hackclub-assets.com/images/1778622317928-2cc1nb.png)

## Point 2 — Stability Without Movable Fins

The second piece of feedback was a concern about how the rocket would remain stable and on course without active trajectory control or movable fins. This was a major concern of mine when I was designing the rocket; however, I have since learned that active stabilization is not necessary for a safe flight.

Boom Boom uses fixed fins, not movable ones, and that is completely normal. Fixed fins are the standard for amateur and high-power rocketry at this scale. The fins provide stability by shifting the Center of Pressure (CP) rearward, below the Center of Gravity (CG). As long as the CG is above the CP by at least one calibre (one body diameter), the rocket is considered stable. When the rocket pitches or tilts even slightly, the airflow hits the fixed fins and generates a strong opposing force that pushes the tail back into alignment with the rest of the rocket, keeping it flying straight up.

This has been verified in OpenRocket and confirmed through the RocketPy simulations shown in previous journal entries. The simulations account for wind, drift, and real-world flight conditions to accurately predict where Boom Boom might end up.

To summarize, the fins on Boom Boom do not move; however, if the rocket pitches or tilts, the resulting aerodynamic force acting on the fins will push the tail back to compensate, restoring stable flight.

**Total time spent: 1.5 hours**
