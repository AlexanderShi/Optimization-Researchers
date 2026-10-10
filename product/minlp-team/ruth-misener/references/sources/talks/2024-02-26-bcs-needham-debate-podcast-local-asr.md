# "The Needham Debate: Optimisation algorithms" (BCS podcast; panel at Ruth Misener's 2023 Roger Needham Award event)

- **What it is**: a 54.5-minute panel recorded at the BCS event where the 2023 Roger Needham Award was presented to Ruth Misener (the award was presented on 10 January 2024 according to Imperial News, 20 Dec 2023). Panel: Ruth Misener; Michael Huth (Head of Department of Computing, Imperial); Timo Berthold (FICO, TU Berlin); Claire Adjiman (Imperial, Sargent Centre); Darren Budd (BASF UK & Ireland). Host: "Brian" (BCS head of content). Opening words by Julia Adamson (BCS).
- **Where**: released 26 Feb 2024 in BCS's podcast "The Gem of all Mechanisms" on Acast. Episode MP3: https://sphinx.acast.com/p/open/s/5e44115dc4ea04b939ea0700/e/65d71cb0dc02e00016bfd8d3/media.mp3 ; feed: https://feeds.acast.com/public/shows/5e44115dc4ea04b939ea0700 ; BCS page: https://www.bcs.org/articles-opinion-and-research/the-needham-debate-optimisation-algorithms/ (dated 27 Feb 2024). Also on Spotify (episode 03QBbuCet8WQYfQub65LzA).
- **Transcript source**: no transcript or caption track exists. This file was produced on 2026-10-10 by research agent 02 with faster-whisper 1.2.1 (model `small.en`, int8, CPU, beam 5, VAD threshold 0.25), after per-0.5 s gain normalisation of the public MP3. Lines are `[mm:ss] text`, as output. Nothing was edited by hand.
- **Reliability: LOW.** Room recording, five speakers, distant microphones. Many words are wrong; some passages were dropped. Treat every line as a lead, not a quotation of record. Known misrecognitions: "Meiser" = Misener; "BSF"/"ESF"/"PSF"/"UDSF"/"S&P" = BASF; "Pico" = FICO; "Express" = FICO Xpress; "Kimo"/"Teemo"/"Timos" = Timo (Berthold); "Chris Lewis" = Chris (Christodoulos) Floudas; "sorting center"/"Simon Center" = Sargent Centre; "deterministic full organization"/"deterministic normal optimization" = deterministic global optimization; "Department of Political Engineering" = Department of Chemical Engineering; "Cambridge Consulting Data Center" = Cambridge Crystallographic Data Centre; "Reaxis" = Reaxys; "Ruby Cedric" = Ruby Sedgwick; "phasing optimization" = Bayesian optimization; "solar development" = solver development; "VHD" = PhD. Unresolved: "Eaton" [44:50] (a former student of Misener's; not identified).
- **Speaker map [inferred from turn-taking, not from labels]**: [00:01-01:32] J. Adamson; [01:34-02:19] host; [02:20-07:16] Misener introduces the panel; [07:17-07:45] host; [07:45-09:43] Misener; [09:43-09:57] host; [10:00-12:41] Budd; [12:42-12:55] host; [12:55-15:47] Berthold; [15:58-16:19] host; [16:19-22:52] Adjiman; [22:56-23:03] host; [23:03-26:55] Huth; [26:55-27:56] host and others; [27:56-31:57] Misener; [32:03-34:37] Adjiman; [34:44-35:06] host; [35:06-36:44] Adjiman; [36:44-38:30] Budd; [38:34-38:46] host; [38:46-42:28] Berthold (largely lost); [42:35-43:31] Huth (question to Misener); [43:33-46:26] Misener; [46:27-46:51] Huth; [46:51-48:44] Berthold; [48:44-49:26] unclear; [49:26-51:22] host and Budd; [51:22-53:25] Adjiman; [53:25-54:04] Budd; [54:04] host.
- **Use**: quoted in `../../research/02-methodology.md` only for Misener's turns, marked "T9, local ASR, attribution inferred".

---

[00:01] Thank you for taking the time to join us this morning to celebrate the achievements of the
[00:18] wonderful Professor Ruth Meissner. So congratulations to you and I just want to say a couple of words
[00:24] about the Roger Needham Award. This was established in memory of the late Professor Roger Needham
[00:30] and it's made annually by BCS for distinguished research contribution in computer science in the
[00:35] UK-based researcher within 10 years of their PhD. So this year BCS awards the Needham Award to
[00:43] Ruth Meisner for her exceptional contributions to identifying and solving fundamental computer
[00:49] science research challenges at the intersection of computational optimization and machine learning.
[00:55] I hope that this big audience, small audience, would join me in congratulating Ruth.
[01:02] So I'm going to present it to you in the box.
[01:09] It's a different format of event this year,
[01:12] so we're really excited that Brian here,
[01:15] our head of content, is hosting this panel discussion.
[01:19] And we've got some amazing guests that have joined Ruth.
[01:23] So we're all looking forward to a really interesting discussion
[01:25] about data-driven optimization and how recent research
[01:28] translates into industry and practical applications.
[01:32] So, Brian, thank you very much, and over to you.
[01:34] Thank you very much, Julia.
[01:36] Yeah, we're all joining in at the meeting Mr. Rube, aren't we?
[01:39] But Rube has worked very hard on this particular event as well.
[01:45] This is the first time we've had a sort of panel discussion
[01:48] associated with it.
[01:49] But he fits in with one of BCS's engines,
[01:51] which is to show the world, hopefully,
[01:54] the effect that academia has and how important it is
[01:58] to popularize computer science.
[02:01] then it was actually quite difficult to do, but we're going to give that a go today.
[02:04] As Julia says, the theme is data-driven optimization,
[02:08] how recent research translates into industry and practice applications,
[02:11] and we're going to discuss also the intersection of research and practice.
[02:15] But as you've so kindly brought the panel together for us,
[02:19] perhaps you could introduce them for us.
[02:20] Yeah, so I wanted to be able to introduce everybody,
[02:22] so thanks for the opportunity.
[02:24] I'm going to start with Claire.
[02:28] Claire is my academic big sister, so I have been hearing about probably from Claire as I've been reading her papers since I'm not going to say how long ago now because I think her today.
[02:39] But Claire, in her PhD, with my late advisor Chris Lewis, made major contributions in deterministic full organization.
[02:52] She then moved here to London, or back to London,
[02:57] because she had everyone here beforehand,
[03:01] to take up a lectureship in the Department of Political
[03:03] Engineering.
[03:05] And we've learned her research is
[03:06] like this perfect sort of coming together
[03:09] of sort of theory and practice.
[03:10] So she does a lot of this molecular systems engineering,
[03:14] which is thinking about sort of how
[03:16] do I want my molecules to be designed
[03:21] so that they are optimal in some sense.
[03:23] And so she comes across the super difficult
[03:26] by level optimization problems
[03:27] and large scale non-linear optimization problems.
[03:32] And the other reason that,
[03:36] or one of the many other reasons that Claire's quite special
[03:39] is that she leads a sorting center,
[03:43] which is this Center for Process Systems Engineering
[03:46] that's joined between UCL and Imperial.
[03:51] What this thing does is that it's a consortium of academics,
[03:56] but then also a lot of interested companies,
[03:59] of which we accept will be a member for one year,
[04:02] and then hopefully for a month.
[04:04] But this is really a place where, at least for me,
[04:09] one of the things I really appreciate in this architecture
[04:11] is the way that I think sort of collaborate with the companies.
[04:17] Darren is the commercial director of BSF, UK and Ireland, so he kind of agreed to come down for today.
[04:30] I've gotten to work with BSF since 2017.
[04:38] And so basically we had this form of thought that we threw out of the water and we made
[04:57] it completely amazing.
[04:58] And then afterwards, we had to start agreeing to work with me more.
[05:04] And so, Darren has a major leadership role at the S&P, of course, but then also has been
[05:12] very helpful in terms of championing the research and sort of making it possible to go forward.
[05:18] For example, our research chair at the
[05:33] it directs the mixed-integer optimization development
[05:38] at FICO Express.
[05:41] So what there is is a human idea of PhDs at the same time.
[05:46] And we were technically on competing software.
[05:50] Maybe.
[05:50] Yeah.
[05:53] And the research that we were doing as PhDs
[05:57] has basically entirely limited the industry at this point.
[06:00] I mean, there's still some still in academics.
[06:03] But it's difficult to do research in this area
[06:07] just because, basically, Timo and colleagues like him
[06:10] have really pushed this stuff forward.
[06:14] So these kind of big teams in optimization,
[06:19] like the one that Timo needs,
[06:21] they really take some of what's been done in academia
[06:26] but then also some of what maybe should have been done
[06:28] academia and make these products that then the SFM and others use and then
[06:37] Professor Michael Huth is my head of department so thank you very much for
[06:45] all the support of this department. In addition to being my head of department, I think I also wrote my
[06:52] first grants with you. So thank you for that. He pulled me on to some initial
[06:58] grants and sort of training meals type things. So Michael has expertise in
[07:04] discrete mathematics and that is optimization related but not quite mixed
[07:11] into your optimization but he knows mixed into your optimization. So thank you for being here as well.
[07:17] Lovely. Thank you very much. Well I think we all had relapsed of that. I think that's an
[07:21] panel. So keep your thoughts rolling for questions as we go through. We can have a
[07:25] combination of some, obviously some academic insights, and the fact that
[07:30] we've also got Timo and Darren with us, means that we can see how things are moving
[07:37] forward, and I think you've learned some lessons from that process as well actually. So maybe we
[07:42] just start, Ruth, with you, just to give us an overview of the work that we've
[07:48] recognize they come from you. So together with the BSF colleagues, we started calling it the data-driven optimization, and I don't know what that means, but basically I do mathematical optimization and I do computational
[08:03] optimization, which is to say that we solve very difficult problems in America that can be focused on optimization problems. We started calling it the in-driven
[08:15] and optimization with the ESF colleagues,
[08:17] basically to try to emphasize the extraneousness
[08:19] of all problems that we get with ESF.
[08:24] And so I would hope that most optimization algorithms
[08:27] are built on data, but somehow we move towards
[08:31] always trying to make it a problem
[08:33] that touches the real world.
[08:35] It gets messier than at least problems that I have
[08:38] looked at when I was saying, oh well I don't really,
[08:40] I can run on something but I don't have the data
[08:42] or something like that.
[08:43] It's always other weird, whatever.
[08:45] I'm working with you all, which actually is a good one.
[08:49] So I work in two kinds of optimization.
[08:53] One is I work in deterministic normal optimization,
[08:57] but which I basically work with first solver.
[09:01] And with that, we are using sort of branch and bounder
[09:05] divided combo algorithms.
[09:07] This is the sort of foundations that Timo
[09:09] bases his team on in terms of the sort of same central ideas.
[09:17] And then the other kind of optimization I look at a lot.
[09:22] And this would be the PSF teams would be basically
[09:30] like a Bayesian optimization or a black box optimization.
[09:34] We could take very expensive ingredients,
[09:36] but we're not necessarily, we don't
[09:38] have an equation necessarily, and we can write down the opinion down.
[09:43] Lovely, thank you very much. So let's look into how some of that has actually applied.
[09:47] Let me perhaps just start with you, Darren. You're in an organization with very deep roots
[09:51] and huge points of data. How you use data optimisation techniques is obviously a key question for you.
[09:57] How are you using this approach?
[10:00] Well, I suppose for the background, first of all, it says that so people who don't be accepted,
[10:04] So we're a global company, founded 158 years ago this year in Germany.
[10:11] So we have about 10,000 people in research, which more or
[10:16] more are being driven towards the digitalization part.
[10:20] Because when we develop our product, so everything we do, and we always say so,
[10:23] we need to gather more and we need to go back every little time.
[10:26] Probably have a bit of that product in the summer.
[10:29] And they will be developed for our company.
[10:31] So typically, our additives or parts would go into a formulation.
[10:36] Those formulations have to be optimized and meet certain criteria.
[10:39] So if you've got an angry chemical product, the light of the farm would say,
[10:45] actually, I want it to be specific on this gene in the farm.
[10:49] Actually, I want it to absorb onto the farm, or maybe I want it to run off part of it.
[10:54] I want it to not drip so much in the wind.
[10:57] And so when we talk about the data in terms of that messy data,
[11:02] it's all coming to a formulation.
[11:04] And they've got to then work with other parts.
[11:06] So in terms of how you then take that data,
[11:09] how you put it into the experiments
[11:11] that we want to drive out.
[11:13] And that's part of how you then put this all together.
[11:15] So we know the experiments we want to do.
[11:17] We know we want to get to it.
[11:18] Sometimes they don't always match up.
[11:20] So how do we then optimize the properties
[11:23] that we want in the product and use then the data
[11:26] to drive that water, to actually get that bottom that we need in the products we're
[11:30] developing.
[11:31] And that's always, and it's a two phase, then once you've got that, then how do you use
[11:35] that data to look at how can you manage that at a cost that actually you did want to buy.
[11:42] So it's not just the product optimizing for the properties, it's actually looking at
[11:48] everything the right way through that process and actually come to the end of the consumer
[11:52] actually, what do they want to drive it back to the wall?
[11:55] So it's not just, okay, starting from the end,
[11:58] it's that whole learning path
[12:00] and then the iteration comes with it.
[12:03] So can the annual processes and organization
[12:05] change into a role of looking into principles?
[12:08] Oh, very much so.
[12:10] And what's the more ways you can use it?
[12:11] Well, we've developed a product which is for our customers,
[12:15] which is an R&D product.
[12:17] So our customers can link into a tool,
[12:19] and they can then come in and put, use their data from that formulation into this and then
[12:26] drive their formulations and let that know happen. So actually it's working, rather than
[12:31] us just making a product which our customers think they need, is that they can actually
[12:35] use their data anonymized in our system to actually help us develop products for that
[12:41] formulation factor.
[12:42] That's interesting. So I think it's all a process of your collaboration as well.
[12:46] Very nice.
[12:47] Thank you, and Timo, FICO is a different sort of organisation, how have you found that this concept of data with an optimization
[12:55] assisting your, I think it was a little bit of your organisation as well. Yeah, yeah, absolutely. So
[13:01] the team that's on Reddit, I'm working on optimization depends a lot on the input data, as you can imagine, so the best
[13:11] optimization model is worth nothing without good data coming into it, and
[13:17] We at Pico, aim for our team is to make this one big streaming process for the consumer
[13:26] for the other team within Pico who look at what data care, data processing and when I
[13:35] joined the company like 10 years ago or so, everything was on-premises like our customers
[13:42] that are mostly working within their own little shell.
[13:46] And Pico has started at that point
[13:49] to put everything cloud-first and to one of the ways
[13:54] to have everything in one big online product
[13:59] where you can continuously integrate new models,
[14:03] change your models, continuously integrate data,
[14:07] process data, get your output, your visualization,
[14:11] And I think that's something that has really changed
[14:14] in the industry that you are going from
[14:18] what, let alone products, models that stay at the same time
[14:22] to continuously changing systems.
[14:26] And then this principle changes with the fact that you
[14:30] process all your data just in time and we can tell you
[14:34] and in missing data, how do you handle data errors?
[14:37] This is where AI has made great contributions in the past
[14:42] to fill in the gaps that we have there.
[14:44] And yeah, that's where we are moving to.
[14:48] And by now, this is by far the biggest part of our consumer
[14:54] is people who work within an online platform.
[14:58] Yeah.
[14:59] You've connected two really far apart talks,
[15:01] they've been there.
[15:02] We were talking about an activity group
[15:03] and then you talked about customer satisfaction.
[15:06] I'm glad to work in a field where the commercial research and development is too close to the
[15:18] academic research and development as Ruth pointed out.
[15:23] So when I transitioned from my PhD where I have been developing a solver to my commercial
[15:31] career, if you wish, where I was developing the software. Eventually, the only thing that I need to change was the keywords and the code that I wrote.
[15:41] It was good everywhere. I was writing Express Express Express and it was easy work.
[15:47] And she was the same as in my academic times, just with slightly different focuses on usability, customer satisfaction, convenience.
[15:58] Really interesting. Thank you. Well, let's let's go let's go back to not back. Let's have a look at the research area
[16:04] So we'll start over with fairs. We can ask you about some how they give not some relation fits into your research
[16:19] So
[16:28] focus on process systems engineering, which really means you're targeted at the process
[16:35] and energy sectors, and we work on computational methods to model, design, and operate those
[16:46] kinds of processes, chemical processes of the type that PSF has, but also, like I said,
[16:51] energy sector and also pharmaceuticals, biological processes, so many things that have some chemistry
[17:00] in them.
[17:01] And so we are about developing methods for this, we are a multithrenary research centre,
[17:09] so we have people from mostly chemical engineers but also computer scientists, design engineers
[17:17] and a few other fields of inquiry.
[17:20] And we have to try and reach the gap
[17:23] between the scientific understanding
[17:25] and the development of methods for decision-making
[17:29] based on that understanding.
[17:32] And so I think it's useful to think
[17:34] about those three elements of modeling, design,
[17:39] and operation, very different in terms
[17:41] of the impact of data driven optimization.
[17:46] So for example, if you issue work on operations,
[17:49] which is actually very familiar to me,
[17:51] but my colleagues work on that a lot.
[17:54] So this is a context where you're operating a process,
[17:59] where the process has control system.
[18:02] So you're limited in terms of the exploration
[18:04] that you can do in that system.
[18:06] But on the other hand, you're generating lots
[18:08] and lots of data, at least in the areas,
[18:10] or even hopefully way more to operate the system
[18:12] rather than in phenomenal situations.
[18:15] And so the challenge there is, you know,
[18:17] how do you use that data to make better decisions,
[18:21] the data that's coming in and to correct any model,
[18:25] plant mismatch that you have,
[18:27] and anything that you haven't accounted for in your models,
[18:31] and how do you both make minute to make decisions,
[18:35] but also make decisions about how to operate that process
[18:38] and improve its performance.
[18:41] At the level of design,
[18:44] tend to be in a space where you have a lot less data which have the ability to explore
[18:49] and so to do experiments and I think there are some fantastic opportunities there from data
[18:55] driven optimization both you know and it depends on what is data driven optimization but I guess
[19:02] I'll define it in a way. So I tend to think of it as you know as I think as Timo said
[19:10] every model, every optimization problem has data in it, in such which all connect to reality
[19:15] that's really important. But I guess you can have different degrees of physical understanding
[19:21] embedded in that optimization problem. So you can go from having non-at-all kind of black box
[19:29] optimization to having very detailed models that we typically work at the level of having
[19:36] the conservation of mass, conservation of energy as the underpinning principles.
[19:41] And we might be using some elements to those models. So you can have hybrid models, you can
[19:46] have quite detailed models where you want to use data-driven optimization to be a surrogate model
[19:52] that can enable you to solve problems that might produce you inaccessible. Or I think at the
[19:59] formulation end of things, for example, or discovery, you want to use data-driven optimization
[20:04] to support looking outside the box, whereas without data remote immunization, you might
[20:09] be just making incremental innovation because you want to be moving close to where you know
[20:16] things are going to work, which is improvement to start with by day.
[20:19] I think with data remote immunization, like Bayesian immunization, you have the opportunity
[20:24] to then do something radical with your experiments and hopefully to get better at immunization.
[20:31] But I think in our field, this needs to remain connected
[20:36] to our physical understanding, because the way
[20:39] that molecules and mixtures behave is so nonlinear.
[20:43] But I think if we try to develop molecules that are completely
[20:47] free of physics, the amount of data
[20:50] that needs to be generated is just intractable.
[20:53] And so we need to learn from what we've done previously,
[20:55] whether on the specific molecules and mixtures
[20:57] that we have or on other ones in the kind of a fancy
[21:00] for development. That is, you need to learn from all of your
[21:07] family to develop, and bring that to bear somehow onto the development
[21:12] molecules. I think the other area of challenge in the chemical
[21:19] industry, in the application of the techniques, the chemical industry, is issues
[21:23] around scale. So a lot of the experiments you do are small scale, but you want to
[21:29] scale up your process, right? So in the lab you're talking about grams, at best
[21:34] kilograms, and then you're talking about tons of hormone you want to scale up, and
[21:39] you come to experiments at that scale, right? So you need predictive models, so
[21:44] you have an issue of how you get the models to extrapolate to a different scale. It's really
[21:50] critical. And same thing if you're thinking about sustainability, and you
[21:54] don't want to think just about, say, your reactor or your crystallizer, you need to
[21:58] think about the whole system and its sustainability and how decisions that you make for one process
[22:04] unit impact on the overall performance. So you might want to compromise on the optimization
[22:09] of your reactor just because your separations for the problem are easier than overall. That
[22:16] means less energy requirement, less material use and better sustainability. So to me,
[22:22] we've got some of the challenges around data and optimization. The scale of the data is often
[22:27] not much to the problem you actually want to solve, do you understand that?
[22:32] Very interesting. So you're taking stuff from that very basic side. If I'm not this right,
[22:36] it seems like you're saying you can't model roundly in motion, you have to take the physics
[22:40] into account.
[22:41] Yes, yes.
[22:42] Okay.
[22:43] There are some things we know, right? And the other models that we use are, you know,
[22:46] and they have a degree of, they're kind of tenable, they're not completely, they're
[22:52] not first principles, but they have some physical principles, nonetheless.
[22:56] Interesting. Thank you. So Michael, we've come to you. Same question really.
[23:00] Each of these institutions is different. Let me tell us how they've driven up the
[23:03] foundation to attend your research. Yeah, thanks Brian. So many private computers
[23:07] within the Imperial College of London, which in itself is a world leading
[23:11] university. So really, you know, we want to do research, led education and our
[23:17] research has to be world leading. And I think maybe you've been there for 22 years now.
[23:21] One distinctive thing I could probably say is that the department has an incredibly strong
[23:27] mathematical foundation, which resonates very well with the scope of the award.
[23:32] So our undergraduate training in particular is really emphasizing a very broad spectrum
[23:37] of mathematics, say, statistics, probabilities, discrete math, logic, and all those kinds of things.
[23:43] And this is going beyond the first two years of studies.
[23:47] And so really, I think our students come out of their training with these incredibly strong foundations in mathematics.
[23:55] But at the same time, they're really engineers, so they have understood how to design systems, to evaluate them, to understand how to scale them up, and so on.
[24:03] And then to actually often use these mathematical foundations to do something new with those systems.
[24:09] And I think this is probably why our undergraduate degree, certainly within the UK, is the most popular one in terms of application numbers,
[24:17] but also in terms of career attractions.
[24:19] And this is certainly something that we want to continue.
[24:22] So in fact, if I see anything strategically there
[24:25] is that the importance of mathematics and foundations
[24:29] and how this sort of blends with computer science
[24:31] and engineering is just becoming ever more important.
[24:34] So I think there's a very exciting time
[24:36] to also head the department with that kind of discipline.
[24:38] So we have, for example, a joint degree
[24:40] with the Department of Mathematics,
[24:43] which is running on a fairly small scale at the moment.
[24:46] But there is a real opportunity here to scale this up
[24:50] and to sharpen the focus maybe on that interface
[24:53] of computer science and mathematics in particular.
[24:56] So, but in a way, I mean, one of the challenges
[24:59] we also have is growing in an institution
[25:02] with limited workspace is very challenging, right?
[25:05] So, and that's maybe also in relation
[25:07] to the British Computer Society.
[25:08] How can we actually make sure that the quality
[25:11] of what we can offer can also be shared
[25:14] other organizations and institutions so that UK students benefit from from these
[25:19] kind of things more broadly. It's interesting, thank you very much. Something that just crossed my mind there about the
[25:26] mathematics being the basis of these things. I was having a conversation recently with
[25:30] someone, if there was a bit more of public understanding of the
[25:34] mathematics behind AR in a large language model, there'd be slightly less
[25:38] imputing consciousness to it and right on the cycle right I guess that's another
[25:42] piece that we have lots of academics who now become sort of ambassadors and have
[25:48] a big voice and we have more colleagues in computing to engage with you know so
[25:52] another 10 Whitehall and so on our own policy also with your organization but
[25:57] I want to make a comment on the research pipeline I think we mentioned that you
[26:02] know with the importance of PhD students so it's absolutely critical I think that
[26:07] we have, you know, financial resources, and also the incentives for people to join at
[26:13] a very early career stage into PhD training. I would say machine learning is still a pay
[26:18] because if they want to have a prosperous career, they kind of have to have a PhD to
[26:23] get into these, you know, companies that I don't want to name at the moment. But in
[26:27] other areas, this is much more challenging. So this is another sort of strategic piece.
[26:32] how can we actually make sure that we widen the talent base
[26:36] and the actual acquisition of young talent
[26:38] who would like to do a PhD?
[26:41] And maybe it's actually a comms piece as well
[26:43] because they might not understand the career opportunities
[26:45] that suddenly open up to that, not just nationally
[26:48] and not just in a specific sector.
[26:50] So that's a problem that we would love to hear
[26:53] some solution of.
[26:55] I think there's probably a role in that sort of
[26:57] compromising that sort of thing.
[26:59] Definitely, yes.
[27:00] I'm not making promises, but that's a good point.
[27:01] Thank you. I think from a company perspective, just to join a company more is really attractive.
[27:07] So I think at Imperial you have to share four DPS days running that company.
[27:12] Yeah.
[27:13] And because that shared input and funding, I think that's really important for us.
[27:20] Yeah.
[27:21] Interesting.
[27:23] So he is one of the PhD students at Warwick, and what he's doing is building on his tools
[27:30] the research that's going on currently, and we think might have a future impact. So we've
[27:43] already seen some examples of research being done, and coming out and further down into
[27:49] the news. That's great. What's next? There's a dinosaur pipeline. What's next in that pipeline?
[27:56] And so with everything that goes on with that collaboration, for example, with Jose, we kind of know the translation already, and with Jose, it's because he's a very late-stage PhD student who has done a ton of work already.
[28:17] a ton of work already, and it's basically mandatory picking which aspects from his PhD
[28:24] does he want to implement. I mean, everything is reproducible, but it is online, but what parts
[28:30] does he want to implement in such a way that it's really, really, like, so solid that, yes,
[28:37] I was going to be using it very quickly in my life. And so the Royal Academy of Engineering
[28:46] grant that I've called with BSF really does enable that plus this really tight
[28:51] connection that BSF has made. Then with sort of where are we going next with
[29:01] phasing optimization, title ideas, Ruby Cedric is here. She just finished her PhD
[29:07] and now she's working on her postdoc. She has this amazing ability to understand
[29:14] by my co-engineers are saying, and then turn it into something that kind of makes sense
[29:19] in respect to mathematics, and then do amazing research that then actually solves the problem.
[29:25] But with that, what we're looking at, or what she's looking at, because she's the expert
[29:32] in the area, is that she's looking at design experiments when we have these quite expensive
[29:42] experiments that involve these many, many different scales.
[29:45] So she's looking at these proteins
[29:47] where you have some sort of a 10 to the some silly number
[29:51] of possibilities, 10 to the 13 more possibilities.
[29:56] And then you can only do experiments
[29:59] on tens of hundreds of outputs.
[30:03] And then you have intermediate information
[30:05] on some of the things in between.
[30:07] And so she's looking kind of at lines
[30:10] with what Claire was saying, how can you put together
[30:15] physical information with experiments and this kind of stuff.
[30:20] And then with respect to sort of integer programming
[30:25] and the kind of stuff that Kimo does, at this point,
[30:31] I don't work as much on solver development, basically,
[30:35] because that part isn't, I don't want to think you can do it,
[30:43] is that sort of the strength of those codes at this point,
[30:50] if I need something who's basically on the inside
[30:54] to help me out with the experiments
[30:56] that we're going to be doing that.
[30:58] But we've been thinking a lot recently
[31:01] about embedding these trained models
[31:06] from machine learning into larger optimization problems
[31:11] and then designing effective algorithms
[31:13] that incorporate these models that we learned from data
[31:17] into sort of the typical integer programming problems.
[31:25] We're really enjoying it and where, you know,
[31:29] basically what it does is it creates these hugely
[31:32] difficult optimization problems that even,
[31:35] that are that solvers like Timos can't or have difficulty with because it's still ugly numerically.
[31:42] Their fault is my fault.
[31:44] So it's basically trying to figure out...
[31:46] Yes, exactly.
[31:48] No worries, they're worth music.
[31:50] But it's basically trying to figure out how to look at that kind of stuff more numerically tractable.
[31:57] And that's what Juan is working on right now with his postdoctoral work.
[32:03] I think I'd like to start by emphasising the, I think, growing importance of industry,
[32:19] academia, collaboration in this context, and broader stakeholder engagement as well.
[32:27] So as Luzh alluded to, she will have a consortium of industrial partners that we've been working
[32:34] with at the Simon Center for many years, some of them since the beginning, which is I think
[32:39] 30 years ago.
[32:42] So that's something that has really shaped our research program and given us the motivation
[32:48] for the kinds of problems that we have to tackle, but I think that relationship needs
[32:52] to evolve now because data, having access to data is becoming so important and so we
[33:00] can no longer use made-up data, for example, to develop point problems. We really do need
[33:06] to have access to a lot more data than we can generate for us. So I think there is a
[33:14] the need for us to get into their own industry
[33:17] to develop data sets that can be used
[33:23] as part of the academic research
[33:25] or the thinking that we've left behind.
[33:28] So I think that's about the information
[33:30] that's really an important part of what I want
[33:33] in search forward and making data-driven optimization
[33:36] something that we can all work on.
[33:39] In terms of the challenges,
[33:40] I would use specific research challenges.
[33:43] I think I would take on some of the things that you have highlighted already, so I think
[33:52] these hybrid models, optimization problems where you have component, which is machine
[33:58] learning models, are really very important for us to work on.
[34:03] Another exciting area is the, I guess, the cyber-physical aspects.
[34:08] So, you know, BSF is working a lot on the idea of, you know,
[34:11] the lives of the future and calculating a system that has
[34:16] physical experiments combined with computational experiments
[34:20] and computational models, and trying to integrate that
[34:22] multi-healing.
[34:23] That's a really fruitful area of investigation in the future.
[34:28] So, we're trying to connect that a bit more.
[34:32] So, to me, those are some of the big challenges.
[34:34] And what I mentioned earlier, the amount of scale of
[34:37] bridging the scale of the data to the actual problem which tends to be much larger scale.
[34:44] I'd say you made an interesting point there that there's like a sort of pseudo bit more data,
[34:48] taking the data that's already in industry and then you get music,
[34:52] because it's real data and it will not trade data or anything like that.
[34:56] Is that difficult? I mean, is it in format that you could actually use?
[35:00] Is there a lot of processing to go on between the data and this is how it can actually use it?
[35:06] Yeah, I mean, I would say it's difficult. So there are some areas where this is very well established.
[35:12] So, for example, I do some work on crystal structure prediction and the Cambridge Consulting Data Center
[35:18] has a wonderful database where anybody who resolves a crystal structure experimentally
[35:25] and is willing to share it publicly submits that to this database and you can access those data
[35:32] accepted standards, so that's the kind of core standards for data.
[35:38] Then I do some work on reaction kinetics, let's say, where there's a huge amount of data in the literature for that,
[35:49] so you have databases like Reaxis, for example, where the information is very patchy,
[35:56] so you might get something like the yield of the reaction, how much of the reaction has progressed,
[36:00] without knowing necessarily how long people waited for that reaction to happen, which in the next later is difficult to use.
[36:08] Sometimes there is no temperature in the reaction procedure, so you're missing a lot of information that is behind those data points.
[36:17] And the other challenge that we have and where industry, I think, can really help us is that a lot of those data are positive data.
[36:25] So, in the sense that you only get reactions with high yield, but the ones with your own yield are missing and it's been for a few papers recently on the impact on that, on the sheer end, it's not food to have that kind of food taken out of course.
[36:40] And so, you know, sheer industry has lots of fun.
[36:44] I think part of that is the way you move from that, and yes we've got a number of it
[36:59] elsewhere, the use alone, and maybe we haven't published it, we're working on it, and that
[37:05] could be, we talked about it earlier, historical, so this could be 20, 30, maybe 40 years old
[37:12] in that notebook, which we haven't accessed yet, and we need to find a way of accessing
[37:17] that data to bring it to the level of finding sense, say, look, how can you help us with
[37:22] this?
[37:23] How can we increase the year?
[37:24] But we didn't have the processes at the time that we needed, how we didn't have the head
[37:29] money, we didn't have the confusion power to it, and now we do.
[37:33] So can't we then go back and mine the masses of actual data that we have, and how do we
[37:40] do that?
[37:41] And in the right format, so it may not be in the right format now what we need, so, and
[37:47] time and effort, so that the new digital lab, the move form, in terms of that digital, so
[37:53] and we are spending a lot of money, a lot of time and resources in terms of moving our
[37:58] physical lab into more digital labs and actually predicting what experiments we need and then
[38:03] actually rather than doing the masses of experiments we did in the past, actually then
[38:07] focusing, I said, what are the threats that we need to do? Actually, we had to train our
[38:12] chemists and physicists and biologists to really understand, and so as a way we could go about
[38:17] the threats. But that takes time, it takes resources. You have a unique problem really,
[38:22] don't you, many ways, isn't it? If you start an organisation 10 years ago and you did so,
[38:25] then you had a problem with it. But you go back to the 1870s, where we were going to do
[38:30] pornography, right? Okay, there you go. Yeah, I did that, I'm ahead, it didn't quite work.
[38:34] Tim, can we come on to you about that as well, as to what you see might have an impact on you in the near future from the research area?
[38:44] I'd like both of your hats on.
[38:46] It goes to the academic and industry.
[38:50] I also want to make sure we get a few of them and supervising PhDs and master's in DIO,
[39:20] which is second and uses of optimization, software, and a lot of research we might see, and so on and so forth.
[42:09] It seems to me, from the idea of doing things in a different way and making sure that commercially,
[42:23] If that general trend is actually in academia,
[42:26] or we have special faith in what we're talking about,
[42:28] you might take it.
[42:35] Yeah, it's definitely a new period.
[42:37] That's sort of how the DNA, I would say, I'm not so sure.
[42:39] I can judge, you know, how this works nationally.
[42:44] Yeah, but I would say maybe on the data-driven optimization
[42:47] and strategic info for the department and the college,
[42:50] you know, this is not just something for a specific sector.
[42:53] We're very grateful for the partnership with UDSF.
[42:56] It's obviously relevant for other sectors,
[42:58] but also it's actually relevant for academic research itself.
[43:00] So if you take, for example, a traditional technology
[43:03] stack or future data centers with these amazing increases
[43:08] of network speeds and so on, it's actually not even clear
[43:10] how to design future data centers,
[43:11] even with this sort of new kit and the new toys.
[43:14] And data-driven optimization will be a key part of that.
[43:17] So that's almost the question to the root,
[43:19] how you can have your traditional customers
[43:22] as sort of industrial partners and maybe sort of clients
[43:26] But they might actually be other academic research groups, you know, so how would you see that, maybe, if I may?
[43:33] So is the question basically translating from one application area to another?
[43:38] Yeah, being almost the user of the sort of state-of-the-art of what you and then you are doing,
[43:44] but maybe not necessary care if something like systems could do systems,
[43:47] but understanding enough to actually use that in your own research,
[43:51] which is traditionally maybe not optimization related.
[43:55] And so the question is, how much do you need, or, well, I think you need a PhD, not from a bank.
[44:01] Okay.
[44:04] I mean, sort of biased and tinny glasses and so forth.
[44:08] I guess, I guess in terms of what does, you know, the tools like what Teemo and, you know, what Teemo needs,
[44:18] they are industry standard, you know, it is a kind of thing where, you know, you don't need a PhD in mathematical optimization
[44:27] to use the kind of tool that Timo develops, and that's honestly, you know, why you all do so well at then selling it.
[44:36] What I find, at least for the people that I get to work with, who, of course, do amazing things, is...
[44:50] so both Eaton and Johannes are here. They did PhDs that were somehow related to chemistry or chemical engineering applications somehow.
[45:04] And now they're effectively doing solar development
[45:07] with respect to supply chain and semiconductor manufacturing.
[45:12] And the thing is, when you're sort of somebody with,
[45:16] when there's somebody who has expertise
[45:20] in the research of optimization as both of them do
[45:23] and in sort of algorithm development,
[45:26] they're both going to be using tools
[45:28] like what Teemo develops,
[45:30] but those problems are so enormous
[45:33] that they cannot help but do solver development
[45:36] effectively on top of what Timo is doing.
[45:39] So they'll kind of be using their solvers,
[45:41] but then they'll also be developing their own algorithms
[45:45] that are in a completely different domain
[45:47] than the research that they did as VHD students.
[45:50] On those postdocs, but then it's a pretty,
[45:56] I get to work with really smart people,
[45:57] so what I say is it's a pretty easy move.
[45:59] I mean, it's a pretty easy move for super talented,
[46:03] But for people who are super talented,
[46:05] it's a pretty easy move to a different application.
[46:11] And then their knowledge of those algorithms,
[46:14] they know where the algorithms are going to be, of course.
[46:17] And then they are changing those algorithms
[46:21] or writing their own things on top
[46:23] to make sure that they're dealing with the bits
[46:26] that they don't really handle.
[46:27] I see.
[46:28] So there's basically higher adoption barriers,
[46:30] I guess, for other research areas,
[46:33] you know, compared to the mechanical machine learning,
[46:36] all the software, you know, has been created
[46:37] in the last 10, 15 years, you know,
[46:39] Keros is just, you know, high torches, two examples, right?
[46:42] So, I guess we're not there yet in that sort of area.
[46:48] But that would be very difficult to get, right, so.
[46:51] What do you mean by T1?
[46:52] I mean, it's one of the things that I was working on,
[46:57] And it has some, I find great approaches in the middle of different teams, and my theme is how to make it all accessible to business users.
[47:08] And so, how can you make optimization work for someone who doesn't want to be achieved?
[47:13] Right.
[47:14] Automation, email master, maybe never really heard from optimization, rather than on a very broad perspective.
[47:22] How can you make this accessible, and still, as a whole machine, we're working on these,
[47:29] and this is what a lot of these platform applications that are inside easy,
[47:36] wireless, very easy applications that you can try to achieve.
[47:40] So, and I think this is one of the things that's fantastic about the new GSA,
[47:46] based on the expert technology, and almost looks like a black box,
[47:52] In many cases, in the most challenging cases, as you pointed out, you would stay into...
[47:58] Do you have a sense, in the user base, what percentage are people who would think of this
[48:07] sort of quite knowledgeable about the optimization, and what percentage are sort of certainly sort
[48:13] of people, but people who are focused really on the application and therefore aren't
[48:17] And we are going to deliver that also interesting and special meeting for us, where we have big
[48:31] money with this project and we can deploy something on a company wide level rather than
[48:40] only to a small expert team within a big company.
[48:44] One, I mean, there's your answer, Michael, right?
[48:46] Yeah, that's fair.
[48:47] I mean, basically, the problems that, you know,
[48:52] people who are going to come to me are going to have
[48:54] some amount of problems, but you're expanding the base.
[49:01] That process has got a habit to come up about public property.
[49:06] Yeah.
[49:07] So, as you were mentioning, the importance of GHE
[49:11] in an organization that was trying to do accounting in the head, I think, in our expert development.
[49:17] In 2015, I adopted 18 people who had a PhD, so, yes, that's been some great career protectors for me.
[49:26] Let's talk about that thing with Darren. Can I bring you in advance on what you look for for BASF,
[49:32] in terms of the kind of people who recruit, what you look for in research?
[49:36] I mean, we're always looking at the talent.
[49:40] War on talent is probably one of our biggest challenges,
[49:44] especially in state-trip optimization
[49:48] or machine learning.
[49:49] Trying to find the right people,
[49:51] the right quality is really difficult.
[49:53] So working with the likes of the imperial,
[49:56] understand what they're doing is part of that.
[49:58] So then setting industry challenges
[50:01] so that we can see where that goes.
[50:03] We don't want to take,
[50:04] and I think we don't want to take all of it.
[50:05] So having the folks root there,
[50:08] actually, we want you to stay there.
[50:10] We want you to develop for the PhD students,
[50:12] the post-docs, because actually we need that,
[50:15] basically we need that relationship
[50:17] between academia and industry.
[50:20] That's really sort of good.
[50:22] And I suppose look randomly, so to understand,
[50:25] so when we look into some of these,
[50:26] in terms of technical abilities, right?
[50:29] So from that, but also in terms of how you translate,
[50:32] so somebody can translate what they're doing
[50:34] into the real world products.
[50:36] So that's why when we do our PhD or post-op messages,
[50:41] we bring them into our labs for three to six months period
[50:45] as well so they get to understand.
[50:47] So that communication is key to translating.
[50:51] So we want to work and say,
[50:53] okay, we want the best people in terms of a high skill,
[50:56] but also people who can work in teams.
[51:00] Teams are important and that's also giving back
[51:02] So we learn as much from Ruth as she does from us as well, and that's really important
[51:09] in terms of that relationship we're building, in terms of the whole realm of the person.
[51:15] So it's not just the knowledge, it's about that person and how we translate the technology.
[51:22] Okay, if you can review on that research properly.
[51:25] Yeah, I think this goes back to the question you were asking about industry and how unique
[51:29] I think the kind of relationships that we have developed are.
[51:34] So as Michael said, you know, I think kind of collaboration
[51:37] between individuals, DNA, and you have to have a culture
[51:43] where you face value of communicating with industry
[51:46] and making the effort to understand
[51:50] and to explain to the understood as well.
[51:53] So I do think we have that culture
[51:55] and I think the decay goes really well
[51:57] this generally speaking. We, you know, we have things like the prospective ownership
[52:03] that ETSL still has. So ETSL is, of course, has a lot to do with individual and others.
[52:11] And those are really big efforts that are co-led by industry and academia,
[52:17] but looking at fundamental research and but also looking at the translation of that research into
[52:22] industry and I think it was a fantastic program and we have one with EIE as well, one with
[52:28] author and gambles. We have a few of those and it's really transformative in terms of the kind of
[52:33] research that you do and the impact that it can have. And then you have things like
[52:38] REF, you know, with impact statements that you give an incentive, essentially to the institution
[52:44] to support translational research into practice. And I think so in the UK I feel it goes really
[52:51] well in that, you know, maybe in a way it's a bit from things like impact factors in journals
[52:58] and you know, publishing in some journals and applying that factor where the work might
[53:04] be more risk-efficient. I don't want to devalue that at all, but I'm saying there's value
[53:10] involved for these activities, and I think you have a broad view as well from your interaction
[53:15] of the universities around the world, and thinking about how they approach industry
[53:21] in their collaboration. I feel that the UK is quite strong on that.
[53:25] Is that your perception there?
[53:26] Yeah, it's different in terms of different parts of the world. I think the format for
[53:32] UK that collaboration is really strong from a UK perspective. We base at Imperial, we do
[53:41] We do go to the University of the UK, but Imperial is our magazine, because of that collaboration
[53:47] nature we have and that interaction, and it's a band of ethos in terms of how do you want
[53:54] to work, how are we at the company, how do we work, and how does the Imperial work, and
[53:58] it just fits, so that's why we've sent it, and that's why we work with Latin Root.
[54:04] It's been a fascinating conversation from my perspective, thank you very much.
