---
title: "Neovim 0.12 极简配置教程 - 10个插件打造高效编辑器"
source: https://www.youtube.com/watch?v=lljs_7xB7Ps
author: Theo
created: 2026-04-10
type: source
tags:
  - neovim
  - vim
  - editor
  - tutorial
---

# Neovim 0.12 极简配置教程

> **视频来源**: [YouTube](https://www.youtube.com/watch?v=lljs_7xB7Ps)  
> **时长**: 62 分钟  
> **主题**: 使用仅10个插件配置Neovim 0.12，打造极简但强大的代码编辑器

## 摘要

这是一个关于Neovim配置的综合教程视频。视频强调在AI代码生成时代，学习编辑器的高效操作（motion、macro、编辑、移动）比以往任何时候都更重要。Neovim 0.12版本内置了插件管理器vim.pack，提供了开箱即用的优秀体验。

本教程展示了如何使用精选的10个插件创建一个极简、可维护且功能强大的Neovim配置，包含LSP支持、linting、格式化、代码补全和美观的status line。

## 章节内容

### 第1章 [0:00 - 12:25]

**开篇**: There has never been a better time to...

- There has never been a better time to
- get into Neoim.
- The impending release of Neoim version
- 0.12 includes its own built-in plug-in
- manager and a lot of other improvements.

### 第2章 [12:29 - 24:42]

**开篇**: to words. So for example, if this had...

- to words. So for example, if this had
- dash in it, this would all be one word.
- So if I hit W right now, it's taking me
- there. But once we apply these settings,
- that's all going to become one word.

### 第3章 [24:45 - 36:41]

**开篇**: can see that we didn't yank that. So...

- can see that we didn't yank that. So
- this is just demonstrating what we had
- earlier. The cool thing about this text
- yank post is that we just get a little
- bit of highlighting for the feedback.

### 第4章 [36:44 - 49:02]

**开篇**: here it has the installation...

- here it has the installation
- instructions. And we're going to install
- it here. And then once again, we're
- going to load it here. Now I've actually
- got a function that I've written for

### 第5章 [49:04 - 1:01:23]

**开篇**: using eslint D for TypeScript,...

- using eslint D for TypeScript,
- JavaScript, but also all those other
- languages that we talked about. Okay.
- And I just realized that I had neglected
- to include Go, which is one of the

### 第6章 [1:01:25 - 1:02:10]

**开篇**: writing or coding, you want...

- writing or coding, you want
- distractionfree, then I think Zen mode
- is an excellent plugin and I use this
- one a lot myself. It basically just
- simplifies the whole UI. It cleans

## 完整字幕

**[0:00]** There has never been a better time to
**[0:02]** get into Neoim.
**[0:04]** The impending release of Neoim version
**[0:07]** 0.12 includes its own built-in plug-in
**[0:10]** manager and a lot of other improvements.
**[0:12]** In this video, I'm going to be walking
**[0:14]** you through the latest version of Neoim
**[0:16]** into your own custom configuration which
**[0:19]** is going to be minimal, tastefully
**[0:22]** minimal, but powerful at the same time.
**[0:24]** You're going to have language server
**[0:25]** protocol support, linting, formatting,
**[0:28]** completion, your own beautiful status
**[0:30]** line.
**[0:31]** Now, there's a twist. We're going to do
**[0:33]** this with just 10 plugins. You can add
**[0:36]** more later if you want, but I want to
**[0:38]** keep this ultra minimal, ultra
**[0:40]** maintainable, and ultra powerful. In the
**[0:44]** age of AI slop, this flies in the face
**[0:46]** of agentic code editors and AI generated
**[0:50]** code. But I want to make a point about
**[0:52]** that. There's never been a better time
**[0:54]** to learn Neoim because the foundational
**[0:56]** thesis of NEOM is about editing code. We
**[0:59]** can generate code faster than ever
**[1:01]** before, but what we're going to be doing
**[1:03]** with Neoim is improving our efficiency
**[1:06]** around motions, around macros, editing,
**[1:10]** moving around the codebase, and that's
**[1:12]** never been more important than in 2026.
**[1:16]** So, with that said, let's get into it.
**[1:20]** All right, team. So, we need to install
**[1:22]** Neoim. Right now, I'm on the Neo Vim
**[1:25]** road map. And if you have a look here,
**[1:28]** you'll see that the current stable
**[1:29]** release is 0.11. And it was a great
**[1:32]** release, but the one that I'm actually
**[1:34]** concerned with is imminent, and it is
**[1:38]** 0.12, the year of Neoim out of the box.
**[1:42]** So, the important thing here with the
**[1:44]** Neoim out of the box 0.12. The most
**[1:47]** important improvement anyway has been
**[1:49]** the addition of a plug-in manager,
**[1:52]** Vim.pack, and we're going to be using
**[1:54]** this plug-in manager to install our
**[1:57]** plugins. There are other UI improvements
**[2:00]** and workflow improvements. And there's
**[2:01]** also the addition of the restart
**[2:03]** command, for example, that allows you to
**[2:05]** restart your NEVM configuration. I'm
**[2:08]** going to link everything of course in
**[2:10]** the video description. But if we go to
**[2:13]** NEVM releases, so this is GitHub NEM NEM
**[2:17]** releases, we can see that there is this
**[2:20]** ENVM development pre-release build. Now,
**[2:22]** it is very mature at this stage. Like I
**[2:24]** said, it's imminent release. And so we
**[2:27]** want to install 0.12. It's just
**[2:29]** important for this tutorial that you've
**[2:31]** got 0.12. Just check with your package
**[2:34]** manager. By the time you're watching
**[2:36]** this, it might already be released.
**[2:37]** Otherwise, you can follow the
**[2:39]** instructions here, which I'll link.
**[2:40]** You've got Windows, Mac OS, Linux, and
**[2:43]** this is a general Linux app image. Now,
**[2:46]** in my case, I'm actually on Arch. So, go
**[2:49]** ahead and choose your installation
**[2:50]** approach. So, I'm actually going to
**[2:52]** install it with Pac-Man. So, I'm on
**[2:55]** Quacios, which is a flavor of Arch. And
**[2:58]** I'm going to install not Nem, but Nem
**[3:02]** Git. So here you'll see that it's saying
**[3:05]** do you want to install the neovit 0.12?
**[3:09]** It doesn't too much matter what the the
**[3:12]** patch version. It's important that
**[3:14]** you're just on one two. So let's proceed
**[3:16]** with the installation.
**[3:22]** Okay. So once it's installed the first
**[3:24]** thing that we need to go is go to the
**[3:26]** entry point. Now for those who of you
**[3:28]** who are not familiar with entry point
**[3:30]** all it is this is just where Neov when
**[3:32]** it starts knows to look for its
**[3:35]** configuration.
**[3:37]** So what we can do we can say mkdir
**[3:42]** and I'm going to say -p for the path.
**[3:44]** We're going to put this into our config
**[3:47]** and then here env. Now I already had a
**[3:50]** directory env but in case you didn't
**[3:52]** that would have created the directory.
**[3:54]** So now what we can do we can actually cd
**[3:56]** into config and neovim and in here I'm
**[4:01]** going to create a new init.lure. So
**[4:05]** we're going to say touch init.l.
**[4:11]** Okay. So now we've created the init.l
**[4:14]** file. And if we have a look in here,
**[4:16]** I've got this in git just so that all
**[4:18]** these changes and everything is tracked.
**[4:20]** Then you can also look up the git link
**[4:23]** so you can see all of the different
**[4:25]** options and the configuration that we're
**[4:27]** going to build in this video. I've got
**[4:28]** an init.l and I've also got a readme
**[4:31]** just so that we can refer back to that.
**[4:32]** Now the init.l at the moment is going to
**[4:34]** be empty. So what I'm going to do first
**[4:36]** of all is I'm going to say envim and
**[4:39]** we're just going to open nvim and in
**[4:41]** here we can just confirm the version
**[4:44]** that we've got and we can see that we've
**[4:46]** got 0.12. So now we can edit that
**[4:50]** init.lure file. Now of course right now
**[4:52]** it's empty. Now remember that I said
**[4:55]** we've only got 10 plugins to play with.
**[4:58]** And one of the first things that people
**[5:00]** will do to make their nem configuration
**[5:02]** look good is to give it a color scheme.
**[5:04]** But actually Neovim has built-in color
**[5:06]** schemes. Some of my favorites are unkai
**[5:09]** and habac. So we can actually look at
**[5:11]** these with the command and then we can
**[5:14]** say color in the American spelling color
**[5:17]** scheme and then in here we can say have
**[5:20]** a max for example. All right. And if I
**[5:22]** wrote in here
**[5:25]** say local test
**[5:29]** function
**[5:31]** and then just say end. Well you can see
**[5:34]** that we've got a certain kind of color
**[5:36]** scheme. Okay. So in my case, I like the
**[5:39]** Hammax color scheme. So I'm going to set
**[5:40]** it to color scheme Havax. I'm also going
**[5:44]** to use term gooey colors just so we get
**[5:46]** the full color support. Okay, the next
**[5:48]** thing is Neoam might be called out of
**[5:50]** the box in terms of the next release,
**[5:53]** but it's already got tons of stuff built
**[5:56]** in. All of this stuff predates Nem 0.12.
**[6:00]** But we're going to set some options
**[6:03]** here. And I've put a description against
**[6:05]** each of them just to make it a little
**[6:06]** bit clearer. Of course though, we can
**[6:09]** use the help built-in help from Neom.
**[6:13]** I'll demonstrate that in a moment. But
**[6:15]** I'm just going to walk you through these
**[6:16]** basic options that I'm going to set.
**[6:19]** Okay. For example, right now on the left
**[6:22]** hand side, we don't have any numbers, no
**[6:24]** line numbers. So, we don't really know
**[6:26]** where we are. We also don't know where
**[6:28]** we are relative to other line numbers.
**[6:31]** We don't highlight the current line,
**[6:32]** although we do have a cursor, but the
**[6:34]** whole line is not highlighted. And by
**[6:38]** default, we're going to not wrap the
**[6:41]** line. So, for example, if you're working
**[6:43]** on a on a large codebase, maybe you've
**[6:45]** got a few panes open. I find it very
**[6:47]** annoying that the code wraps. And so, by
**[6:51]** default, I'm not going to have it wrap.
**[6:53]** Although we're going to look at some
**[6:54]** edge cases later with text where we do
**[6:57]** want it to wrap. Scroll off means that
**[6:59]** if you get within 10 lines of the bottom
**[7:02]** or 10 lines at the top, then we're going
**[7:04]** to keep the cursor 10 lines away from
**[7:08]** the top or the bottom, but keep
**[7:09]** scrolling up or down. And the side
**[7:12]** scroll is going to be the same, 10
**[7:14]** columns to the left or to the right.
**[7:16]** Now, this stuff is about the tabs. Now
**[7:21]** my preference is to have the tabs are
**[7:23]** going to be actually two spaces and all
**[7:26]** of these are actually just to achieve
**[7:28]** that. Now if you want you can have a
**[7:31]** look here. This is probably a good time
**[7:33]** to have a look at the help and we can
**[7:35]** for example look at tab stop and in here
**[7:39]** it's going to give us some better
**[7:41]** description. So for example, tab stop or
**[7:43]** TS for short in here. It's going to
**[7:46]** define the column multiple used to
**[7:48]** display the horizontal tab character.
**[7:51]** Okay. So in my case, I just want it to
**[7:53]** be two. Two horizontal tab characters.
**[7:57]** Okay. So if any of these are kind of
**[7:59]** unclear, go ahead and have a look at the
**[8:02]** help shift width. So obviously that
**[8:05]** pertains to the shift width. So tab is
**[8:08]** going to be two horizontal spaces. Shift
**[8:10]** is going to be two. And then we're going
**[8:12]** to have a soft tab. That's just where
**[8:14]** maybe you have like a lot of empty white
**[8:17]** space. And hitting backspace or tab is
**[8:19]** going to be two spaces there. And we
**[8:22]** want to expand using spaces instead of
**[8:26]** tabs. We want that smart auto
**[8:28]** indentation which inherits from
**[8:31]** surrounded context and we want it to
**[8:34]** indent from the current line. Next part
**[8:36]** is around search. So we've got ignore
**[8:38]** case. So by default if I search for
**[8:40]** something say if I said case insensitive
**[8:45]** okay then it's found that if I now use
**[8:48]** case insensitive with a capital which is
**[8:50]** the smart case which is the next one
**[8:53]** then it's going to become sensitive to
**[8:56]** the case. So by default you can just
**[8:58]** search for everything in lowerase and
**[8:59]** that's going to grab all uppercase. But
**[9:02]** if you start using uppercase then it's
**[9:04]** going to be narrower.
**[9:07]** I also want to highlight my matches on
**[9:09]** search. So if I said for example forward
**[9:11]** slash and I said vim.opt. Now you can
**[9:14]** see all of the matches are highlighted.
**[9:17]** And I want it to be incremental. So we
**[9:20]** just saw as ink search. We see that it
**[9:26]** highlights as it increments. On the left
**[9:29]** hand side you're going to see a sign
**[9:32]** column. And then at 100 characters
**[9:34]** across, I want there to be just a subtle
**[9:38]** line just to indicate that this is 100.
**[9:40]** You could put it at 80 or 120.
**[9:42]** Everyone's got their own preference. And
**[9:44]** in a moment, we're going to save this.
**[9:45]** And all of this is going to become a lot
**[9:47]** more interesting because all of these
**[9:49]** options that I'm describing here are
**[9:51]** going to be applied. Okay. And we're
**[9:53]** going to show the matching brackets.
**[9:56]** We're going to have a single line
**[9:57]** command height. We've got some
**[9:59]** completion options here. So, for
**[10:01]** example, when we tab and what options
**[10:03]** are going to be shown in the completion,
**[10:05]** we don't want to show the mode because
**[10:07]** we're actually going to build our own
**[10:08]** custom status line. And then we've got a
**[10:11]** few items here around the pop-up menu in
**[10:15]** terms of its height when the completion
**[10:17]** comes up and as well as its transparency
**[10:20]** and that kind of thing. Okay. And then
**[10:22]** here we've just got some behavior around
**[10:24]** the performance and also hiding of
**[10:27]** characters. For example, I want this
**[10:29]** tilda not to show up on the left hand
**[10:31]** side. And I want to set a few
**[10:34]** performance parameters here, including
**[10:37]** the conceal cursor. The next thing is
**[10:40]** when we go into a file, we want to have
**[10:43]** an undo directory. And we want that to
**[10:46]** persist. So, not just when you go to the
**[10:48]** file and then you leave that file, but
**[10:50]** later when we come back to a file and we
**[10:53]** want to undo something that we did
**[10:55]** earlier, we want to save that into the
**[10:58]** undo directory or the undo deer. And so,
**[11:00]** the first thing that we need to do to
**[11:01]** make sure that this works is we need to
**[11:04]** create an undo directory. And I'm just
**[11:07]** going to put that in vim undo dear. You
**[11:10]** can put it wherever you want. In my
**[11:12]** case, I think that's totally fine. And
**[11:14]** so what this does is it just goes and
**[11:17]** creates it if it doesn't already exist.
**[11:19]** Now I'm only going to have undo. I'm not
**[11:21]** going to have backup. I'm not going to
**[11:23]** have any swap files, but I am going to
**[11:26]** have the undo file. I'm going to
**[11:27]** stipulate where that directory that I
**[11:29]** want to save those undos to is. And then
**[11:32]** I've got a few items here about
**[11:33]** completion timeout. And auto read is
**[11:37]** important because let's say we have
**[11:38]** another process somewhere and that is
**[11:41]** manipulating the file that you're
**[11:42]** working on. What's going to happen is
**[11:44]** that it's going to auto reload if
**[11:46]** changes have been imposed on that file
**[11:49]** or that file has been manipulated by
**[11:50]** another process outside of NEM. And I
**[11:53]** don't want to have autosave because I'm
**[11:55]** going to have format on save. We're
**[11:57]** going to get into that later when we get
**[11:58]** to the LSP section. Okay. So, we're
**[12:01]** going to allow hidden buffers. We're
**[12:02]** going to have no error bells because
**[12:05]** it's annoying when there's sound coming
**[12:06]** from the computer, frankly. We're going
**[12:08]** to have better backspace behavior. So
**[12:11]** this is kind of in that same line as the
**[12:13]** tabs. It could even be in that section.
**[12:15]** I don't want it to automatically change
**[12:17]** the directory. If I'm working from a
**[12:19]** certain directory, I want that to be the
**[12:21]** base of where I am working from. And
**[12:25]** then I'm going to also append the dash
**[12:29]** to words. So for example, if this had
**[12:34]** dash in it, this would all be one word.
**[12:36]** So if I hit W right now, it's taking me
**[12:38]** there. But once we apply these settings,
**[12:40]** that's all going to become one word.
**[12:44]** And here's some search items. So I'm
**[12:46]** going to include subdirectories in a
**[12:48]** manual search selection. I want it to be
**[12:50]** inclusive. So for example, if I go into
**[12:53]** visual mode, and then I'm going to
**[12:55]** select this. I want that to be
**[12:57]** inclusive. I want it to grab everything
**[13:01]** up until where my cursor is. If it was
**[13:03]** exclusive, it wouldn't include that last
**[13:05]** double quote character. And so I'd have
**[13:07]** to do that in order to select it all.
**[13:09]** I'm going to use the mouse support. Not
**[13:12]** often, of course, that kind of flies in
**[13:14]** the face of what Neo is for, but
**[13:17]** sometimes it's handy just to adjust
**[13:19]** certain panes and that kind of thing.
**[13:22]** And I'm going to make sure that I append
**[13:24]** to the clipboard. Finally, we're going
**[13:26]** to allow for buffer modifications.
**[13:30]** And we're going to set the encoding to
**[13:35]** UTF8.
**[13:37]** Now, it's been a while since I created
**[13:38]** this gooey cursor setting, but what it
**[13:40]** does is it main makes it always be a
**[13:43]** block and it makes sure that it blinks.
**[13:45]** I like it to blink to give me feedback
**[13:47]** that my system's still up. All right.
**[13:49]** And just wrapping up with the options.
**[13:51]** We're going to have fold method. So,
**[13:53]** we're going to you can use folds in NEM.
**[13:56]** And I'm going to actually use tree
**[13:59]** sitter and we're going to install tree
**[14:01]** sitter later including with the new
**[14:03]** updated API. Okay. When we split, say we
**[14:08]** horizontally split, we want the new pane
**[14:09]** to be on the bottom. And when we split
**[14:11]** vertically, we want the new pane to be
**[14:13]** on the right. And I've got a few
**[14:15]** completion options down here, including
**[14:18]** some performance parameters. All right,
**[14:20]** so everything's done. And as I
**[14:22]** mentioned, we've got a new option. We
**[14:24]** can hit restart in Nevim. And now I'm
**[14:29]** going to edit the internet.lure. And
**[14:31]** immediately you can see that we've got
**[14:33]** our color scheme has been applied. And
**[14:36]** also we've got all these nice lines.
**[14:39]** We've got this column over here telling
**[14:41]** us that's 100 characters. We have the
**[14:44]** line that we're on has been highlighted
**[14:47]** and we know that we're on line seven.
**[14:49]** We've got relative line numbers. And of
**[14:51]** course there's a lot more stuff that we
**[14:53]** set here. and that wouldn't be
**[14:54]** immediately apparent, but these are kind
**[14:57]** of the foundational settings for our
**[14:59]** project. All right, so the next thing I
**[15:01]** want to do is I want to create a custom
**[15:04]** status line. So, like I mentioned, we've
**[15:06]** already used the builtin custom color
**[15:09]** scheme. And we don't want to use too
**[15:11]** many plugins. So, I'm going to actually
**[15:13]** create my own status line. At the
**[15:14]** moment, it's looking pretty basic down
**[15:16]** the bottom here. And so, I'm going to
**[15:17]** create one which includes support for
**[15:19]** git. That's the first thing here which
**[15:21]** we're doing is we're going to go and get
**[15:24]** the git branch and we're going to find
**[15:27]** out what the icon is, right? And so
**[15:30]** we're going to include our git status in
**[15:34]** our status line which we're building
**[15:36]** ourselves. And then the next thing we're
**[15:37]** going to do, I want to know which kind
**[15:39]** of file I'm in. And what I've done is
**[15:41]** I've tried to go away and I've got all
**[15:43]** of these different files. So for
**[15:46]** example, we got the lure icon, Python,
**[15:48]** JavaScript, TypeScript,
**[15:52]** CSS, Markdown, Vim, Bash, Rust, Go, and
**[15:55]** so on. I've tried to get as many as I
**[15:57]** can here because I don't want to
**[15:58]** introduce more dependencies. I want to
**[16:01]** have a minimal configuration that's
**[16:03]** highly maintainable than we've got a
**[16:06]** default one down here. But what we do is
**[16:09]** this is a function. It looks up the file
**[16:11]** type from the Vim API and then based on
**[16:15]** that it looks into this table and it
**[16:18]** says okay give us the file type. Okay,
**[16:22]** we're also going to look at the file
**[16:23]** size. So in a moment we're going to use
**[16:25]** all these functions and we're going to
**[16:28]** get the file size and we're going to get
**[16:30]** some basic formatting. Is it megabytes?
**[16:32]** Is it kilobytes? How big is this file
**[16:33]** that we're in? And then before in the
**[16:36]** options, we actually disabled the mode
**[16:38]** because I want to have my own custom
**[16:40]** mode. And I've got some nice icons once
**[16:42]** again to go with that. All right. And so
**[16:45]** what we're going to do, we're going to
**[16:46]** say append this. If you ever see this
**[16:49]** underscore, capital G, that just means
**[16:51]** that this is a global variable. And
**[16:53]** we're going to be applying the mode
**[16:55]** icon, the git branch, the file type, and
**[16:57]** the file size. And so this finally down
**[17:01]** the bottom is our function that applies
**[17:03]** all this. So for example, we're going to
**[17:06]** call it setup dynamic status line. When
**[17:09]** we enter the window, when we enter a
**[17:11]** buffer, it's going to call this. And
**[17:13]** this is an auto command. And that's
**[17:15]** going to call all of our different
**[17:17]** functions. So for example, our mode
**[17:20]** icon, it's going to call our git branch
**[17:22]** function. It's going to call our file
**[17:24]** type and our file size. And by doing
**[17:27]** that, it's going to give us a really,
**[17:28]** really nice status line. The last thing
**[17:31]** you got to do is just call that. So,
**[17:32]** let's go and let's write and then let's
**[17:35]** restart
**[17:37]** and we'll go to our file. And we can see
**[17:40]** down the bottom that we've got this much
**[17:42]** nicer status line. So, if I go to the
**[17:46]** bottom where we were and I can go into
**[17:48]** insert mode, it's going to give us an
**[17:50]** icon, tell us that we're insert mode. We
**[17:51]** know that we're in a lure file. We know
**[17:53]** this lure file is about 8 kilobytes. The
**[17:56]** this is a git repository. We know which
**[17:58]** branch that we're on. And finally, we
**[17:59]** know the path of this file. So this is
**[18:02]** we've just built it ourselves. We still
**[18:04]** haven't introduced any dependencies and
**[18:06]** it's already starting to look super
**[18:08]** usable. Now the next section is going to
**[18:10]** be key maps. I use the space for my
**[18:15]** leader and my local leader. Now some
**[18:17]** people might find that this conflicts.
**[18:19]** So obviously use the approach that you
**[18:21]** want. And for those noobs out there, the
**[18:24]** leader is just the main key that we
**[18:26]** press before we hit some other key to
**[18:29]** make a sequence. And so we're going to
**[18:32]** reference that leader in all of these
**[18:33]** key maps or these key shortcuts. The
**[18:36]** first thing that I'm going to do is I'm
**[18:38]** going to set better movement in wrapped
**[18:42]** text because I use Neovim to write notes
**[18:44]** and to draft YouTube scripts and that
**[18:46]** kind of thing. I have a lot of text. On
**[18:48]** the right hand side here, I've got some
**[18:50]** text. Now, when you're working with text
**[18:52]** in NEM, the default behavior is kind of
**[18:55]** annoying because see here when I'm I've
**[18:58]** got all this text wrapped. So, if I set
**[19:02]** this to its default, so by default, it's
**[19:04]** not wrapped. But because it's text, I
**[19:06]** want to wrap it. And now when I hit
**[19:09]** here, it actually just takes me to the
**[19:11]** next block of text. It doesn't actually
**[19:13]** take me line by line. See, this is
**[19:15]** actually line three and this is four.
**[19:17]** But because it's wrapped, it's actually
**[19:19]** from our user standpoint, that's not
**[19:21]** really the line. So what I'm going to do
**[19:23]** is I'm going to apply this.
**[19:27]** And this is the same thing as saying GJ
**[19:30]** GJ GJ. So when you prefix something with
**[19:33]** G, it's actually just going to go to the
**[19:36]** next line rather than shifting all the
**[19:38]** way to the end of that block. All right.
**[19:40]** So that's the first setting. Next, we've
**[19:44]** got setting for when we've gone and done
**[19:46]** a search. I want to hit leader C, so
**[19:49]** space C in my case, to clear the search
**[19:52]** highlight. So, at the moment, we've got
**[19:53]** key map, right? And I'm going to hit
**[19:55]** that. And now, key map's no longer
**[19:57]** highlighted. I also want the next item
**[20:00]** to be in the middle. So, when I hit N, I
**[20:03]** want it to be in the middle of the
**[20:06]** screen. So, ZZ is to center something.
**[20:09]** And so when I search, let's say we go to
**[20:13]** opt.
**[20:15]** Okay, now we're at the top here. But for
**[20:17]** example, it's always going to keep us in
**[20:19]** the very middle. Same thing when we do
**[20:22]** Ctrl D for down and controll U for up. I
**[20:26]** want us to always be in the center just
**[20:27]** so we can keep our eyes in the center of
**[20:29]** the screen. We're not moving around
**[20:30]** looking for stuff too much. Next is
**[20:32]** leader P. So what I'm going to do is I'm
**[20:34]** going to
**[20:36]** paste without yanking what I've
**[20:37]** selected. And the same thing goes for
**[20:41]** deleting without yanking. And this is
**[20:44]** going to be cool later because we're
**[20:46]** going to highlight the text on yank.
**[20:47]** Once again, not using a plug-in, but the
**[20:49]** cool thing is that what we're doing is
**[20:52]** we're going to highlight and I'll be
**[20:53]** able to demonstrate this. We've got two
**[20:57]** here for the next and the previous
**[20:58]** buffer. So leader BN for next, BP for
**[21:01]** previous. And then when we've got a
**[21:04]** bunch of windows, then we can simply
**[21:06]** move between them.
**[21:10]** and so forth. So just then I'm going to
**[21:14]** go to BN and that's going to take us
**[21:16]** through all of our buffers and we're
**[21:19]** back in that text. Okay. So when we
**[21:21]** split I'm going to use leader SV and
**[21:25]** leader SH to split vertically and
**[21:28]** horizontally.
**[21:30]** And we can also resize. So if we went
**[21:32]** here then we can simply hold control
**[21:38]** and if we had vertical.
**[21:48]** Now one cool thing I do like to rag on
**[21:51]** VS Code a lot but for example one one
**[21:53]** thing I liked was if you hit alt then
**[21:55]** you can shift this line around and
**[21:58]** that's what this section does. I can
**[22:00]** also select all of these and shift them
**[22:02]** all up or shift them all down. That's a
**[22:05]** nice useful thing. And then if we select
**[22:10]** something, the behavior we want is like
**[22:12]** shown because I've already restarted.
**[22:14]** But if we didn't have this set up, what
**[22:16]** would happen is we would indent and then
**[22:19]** it would be deselected. We'd have to
**[22:20]** select again, indent, and so forth. just
**[22:23]** keeps that selection so that you can
**[22:25]** continuously indent or uh bring it back
**[22:29]** towards the left hand column. One other
**[22:32]** thing if we sometimes we might use
**[22:34]** capital J now capital J it just keeps
**[22:38]** the cursor position. So for example if I
**[22:41]** say J it's just going to put it on the
**[22:44]** one line but keep our cursor position.
**[22:46]** Then I have a function here which is
**[22:49]** going to copy the full path. So for
**[22:51]** example, I want to see it and just then
**[22:53]** it just I just did lead a PA and then it
**[22:56]** pasted it. And now I can also paste it
**[22:58]** here. Not that that is uh all that
**[23:01]** interesting. But a lot of the time when
**[23:03]** you need to know the path of the file or
**[23:04]** whatever, maybe a colleague is asking
**[23:06]** where's the location, you can just
**[23:07]** quickly grab it. And sometimes when
**[23:10]** you're writing or you're coding, you
**[23:12]** don't want the diagnostics to be
**[23:13]** enabled. And so I'm going to set leader
**[23:15]** TD to disable or enable the diagnostics.
**[23:19]** That's going to make more sense later
**[23:20]** when we get to the section on
**[23:22]** diagnostics. Okay. In the next section,
**[23:24]** we're going to be talking about auto
**[23:26]** commands. Auto commands are just
**[23:28]** triggered on a certain event and then
**[23:30]** they run a certain action. That could be
**[23:32]** formatting code, that could be applying
**[23:35]** options, whatever it is. And so here
**[23:38]** I've got a few. The first one I want to
**[23:39]** highlight is text yank post. So let me
**[23:43]** apply this one. I'm going to write and
**[23:44]** I'm going to restart. Okay. And so I've
**[23:46]** restarted. And what I want to do, I want
**[23:48]** to show you that now when I select all
**[23:51]** this and I yank it, we are going to have
**[23:54]** six lines yanked. And if you saw that
**[23:56]** just then, it visually flashed a
**[24:00]** slightly different color for a moment
**[24:01]** just to indicate to us that that had
**[24:03]** been done. Now, I said that I was going
**[24:04]** to demonstrate how we can paste without
**[24:08]** yanking or we can delete without
**[24:09]** yanking. Okay, so let's say I yank this
**[24:12]** highlighted yank text. Okay. And I'm not
**[24:15]** going to include the comment. Shift Y.
**[24:18]** And now I'm going to go to the register.
**[24:20]** And we can see that this is the most
**[24:23]** recent one. Right. So I don't want to
**[24:26]** override that. And so what I'm going to
**[24:28]** do, I'm going to visually select this.
**[24:32]** Okay. And now I'm going to use let's say
**[24:35]** we're going to delete or we're going to
**[24:37]** we're going to paste. So we're going to
**[24:38]** say leader P. Okay. We replaced it. But
**[24:42]** let's see if we go to our register, we
**[24:45]** can see that we didn't yank that. So
**[24:48]** this is just demonstrating what we had
**[24:49]** earlier. The cool thing about this text
**[24:52]** yank post is that we just get a little
**[24:54]** bit of highlighting for the feedback.
**[24:55]** All right, then this section is all
**[24:57]** about returning us to the last cursor
**[25:00]** position. So I'm going to quit
**[25:02]** everything
**[25:05]** and I'm going to go back. And as we saw
**[25:07]** just then, I ended up exactly where I
**[25:10]** was in the file before I left. So this
**[25:13]** just restores the last cursor position.
**[25:15]** There are some exceptions. For example,
**[25:17]** in diff mode, we don't really want that
**[25:20]** just to be aware. But ultimately, the
**[25:22]** purpose of this is just to return us to
**[25:24]** the last position, the last time that we
**[25:26]** were in Neo of them in this file. Okay.
**[25:28]** Now sometimes when I'm writing I want
**[25:31]** based on the file type of being a
**[25:33]** markdown or text or git command I don't
**[25:36]** want to wrap the text I do want a line
**[25:38]** break and I also want spelling. So let's
**[25:41]** demonstrate this. I'm going to quit out.
**[25:43]** I'm going to go to the text or and here
**[25:46]** we can see that we've got spelling on.
**[25:50]** So it's giving us a lot of errors
**[25:51]** because there's obviously dummy text and
**[25:53]** it's wrapped. So the cool thing is that
**[25:56]** this was based on the file type the MD
**[25:58]** the markdown file type and that is just
**[26:02]** kind of a quality of life thing when
**[26:04]** you're using Neovm to write a lot as
**[26:06]** well. Okay, so until now we've been
**[26:08]** getting away with no plugins and you've
**[26:12]** already got a pretty powerful
**[26:13]** configuration at this stage but I guess
**[26:16]** I'm a little bit of a there's still a
**[26:18]** little bit of the soy dev in me from my
**[26:19]** early days with Atom and VS Code. I like
**[26:22]** having the tree on the lefth hand side
**[26:24]** even though net RW which is built in
**[26:26]** with nem is really capable but I just
**[26:28]** like being able to see them all. I
**[26:31]** actually never use it because I use FCF
**[26:33]** lure for a fuzzy finder which we're
**[26:35]** going to get into later but I still just
**[26:37]** have it. So this is going to be the
**[26:39]** first plugin that we're going to apply
**[26:41]** and I'm going to obviously include more
**[26:44]** but I just want to demonstrate. So here
**[26:46]** we're using the vim pack and add command
**[26:49]** and we're providing the GitHub URL. This
**[26:52]** is the documentation on the left hand
**[26:53]** side or nvim tree and I've created a
**[26:57]** custom function and what this does is it
**[26:59]** actually calls pack add and then the
**[27:02]** name of our plugin. All right or our
**[27:04]** package. So the first one up here, it
**[27:07]** actually adds it or installs the plugin
**[27:10]** using the full GitHub URL and the second
**[27:13]** one adds it so that when it's loaded,
**[27:15]** depending on whether it's optional or
**[27:17]** not, we're assuming here that it's
**[27:19]** optional, then we can actually see it.
**[27:22]** So going to restart. If you want to see
**[27:25]** where it installs these plugins to, you
**[27:28]** can actually echo and then amperand and
**[27:30]** then packpath.
**[27:32]** Okay. And then here we can see that
**[27:34]** there's a bunch of stuff, but
**[27:36]** importantly we've got the local share
**[27:40]** envim site. All right, let's go and have
**[27:43]** a look at that.
**[27:45]** So if you want to see where your
**[27:47]** packages are going to be installed,
**[27:49]** they're going to by default be under
**[27:52]** local share nim site pack core and opt
**[27:57]** and opt is for optional. So when you
**[27:59]** install a package, it's going to be in
**[28:01]** the optional directory. That's why we
**[28:02]** need to invoke pack ad because pack ad
**[28:05]** actually loads that plugin. So let's
**[28:08]** open up neim and it's going to say the
**[28:11]** plugins these plugins will be installed.
**[28:14]** Do you want to install them? So we've
**[28:15]** got nvim tree which we just added
**[28:17]** already. So I'm going to hit yes. It's
**[28:20]** going to install the plugins. Okay it's
**[28:22]** installed. In order to use it we're
**[28:24]** going to have to call setup on nvim tree
**[28:26]** and then we're going to have a key
**[28:27]** binding so that we can actually open it.
**[28:29]** So let's go back to our configuration.
**[28:32]** All right. So we're back here and what
**[28:35]** we need to do is we need to as I
**[28:36]** mentioned we need to call setup and we
**[28:38]** also need to have some keybind so that
**[28:40]** we can open our neov tree or envim tree.
**[28:44]** Okay. And so I'm going to be expanding
**[28:46]** on this plug-in section. And so I'm
**[28:48]** going to put the configs under another
**[28:50]** header just so it's easier for you to
**[28:52]** navigate in GitHub later. But what we
**[28:56]** need to do is we got to require NVM
**[28:58]** tree. I'm going to set it up. I've got
**[29:00]** some basic things here. I want to set
**[29:01]** the width. And then I also want the dot
**[29:03]** files to be shown. So dot files false.
**[29:06]** It doesn't filter them out. Okay. And
**[29:08]** then finally, we're going to have leader
**[29:10]** E. That's going to be E for explorer.
**[29:13]** I'm going to write this file and I'm
**[29:15]** going to restart. Go to my file. And now
**[29:20]** when I hit E, we can see that we're in
**[29:22]** the explorer. Okay. And just while we're
**[29:25]** here, I'm going to just show you an
**[29:27]** interesting thing. If we have a look at
**[29:29]** the NVIM pack lock, if you're familiar
**[29:32]** with lazy, this is keeping the version
**[29:34]** for you and it's recording the plugins
**[29:36]** that we've installed. All right, so
**[29:37]** noting that we got our NVIM tree set up
**[29:40]** and working, let's get on to the next
**[29:42]** plugin. All right, so the next one is
**[29:44]** going to be FCF Lure, which is a fuzzy
**[29:46]** finder. And we're going to be using this
**[29:48]** fuzzy finder. I use it a lot in my
**[29:51]** projects. So the docs are on the left,
**[29:53]** the GitHub, and in here I'm just adding
**[29:56]** it once again. Vim pack add. And then
**[29:59]** I'm calling it down here. So this is
**[30:01]** going to install it. This is going to
**[30:03]** invoke it. And then we got to give it
**[30:05]** some setup options. So for example, I'm
**[30:07]** going to set it up. And then I've got
**[30:08]** some key maps here. So for example,
**[30:11]** leader FF is going to be to find files.
**[30:14]** FG is to GP. And then we've got FB to
**[30:17]** look at the buffers that we can shift to
**[30:20]** quickly. FH is to look at the help tags.
**[30:22]** FX is to look at the diagnostics in the
**[30:24]** document. And F capital X is for the
**[30:27]** diagnostics in the workplace. So, of
**[30:28]** course, there's plenty more stuff. You
**[30:30]** can check out the documentation. This is
**[30:32]** just the stuff that I use. Optionally,
**[30:34]** you can use webdev icons, but because,
**[30:37]** like I said, I'm going for a minimal
**[30:39]** configuration,
**[30:40]** which is 10 plugins or less, I'm
**[30:43]** actually not going to be including the
**[30:45]** webdev icons. But that's that's totally
**[30:47]** up to you. So, I'm going to exit out.
**[30:52]** It's going to ask us to install. We're
**[30:53]** going to confirm. Okay. And so, now if
**[30:55]** we wanted to, we can say use leader FG
**[30:58]** to GP. And I'm going to say vim.opt.
**[31:02]** And we can see all of the options. And
**[31:04]** of course, at the moment, this is a
**[31:06]** super small project. It's just in a one
**[31:07]** file. We could have just used search to
**[31:09]** do the same thing. But when you're in a
**[31:11]** massive codebase, this is pretty handy.
**[31:12]** All right. So the next one is kind of a
**[31:15]** cheat code because mini env is indeed
**[31:18]** actually a library of 40 plus
**[31:21]** independent lure modules. So it improves
**[31:24]** Neov's experience massively. So even
**[31:27]** though we're only going to have 10
**[31:28]** plugins, there's all these mini plugins
**[31:30]** that I'm going to use here and it'll
**[31:32]** make sense in a moment. So once again,
**[31:34]** we're adding it here to install it and
**[31:36]** then we're calling it with the pack ad
**[31:38]** to load it when we open Nem. And down
**[31:41]** here, what I'm going to do, just going
**[31:43]** to paste in the require. So, just a
**[31:48]** quick kind of look at these. AI is not
**[31:51]** artificial intelligence, but it around
**[31:54]** inside. So, this is going to be good for
**[31:56]** visually selecting or looking at the
**[31:59]** different objects that we are able to
**[32:02]** navigate through. And in a moment, we're
**[32:04]** going to install tree sitter, which is
**[32:05]** going to give us highlighting and better
**[32:07]** control and navigation around these text
**[32:09]** objects. Comment is obviously for
**[32:11]** commenting.
**[32:13]** So you can simply hit GCC and we've got
**[32:17]** better comments. Move, surround, cursor
**[32:19]** word. I would kind of encourage you to
**[32:21]** check these all out in your own time.
**[32:24]** The indent scope, it's going to show you
**[32:26]** where there's trailing space, the
**[32:27]** indentation, the pairs to highlight the
**[32:29]** pairs, uh notify, and also icon. So it's
**[32:32]** got a mini icon set. So, I'm going to
**[32:36]** exit out.
**[32:41]** I'm going to install. And it looks like
**[32:43]** I actually made a mistake when I was
**[32:47]** adding it up here. It's not mini- nvm.
**[32:49]** It's just mini.nv. So, let's try that
**[32:52]** again. So, we can see it's been loaded.
**[32:56]** And we've got the trailing space. If we
**[32:59]** did this here, we can see it's not
**[33:01]** immediately apparent, but we've got some
**[33:03]** nice things like just this is just junk
**[33:07]** code obviously, but this is giving us
**[33:08]** nice indentation. These lines are
**[33:10]** indicating where everything is at the
**[33:12]** end here. If I did that, I get red to
**[33:15]** indicate this is trailing white space.
**[33:17]** So, this is all stuff which mini.nv has
**[33:20]** added. And please do go and check the
**[33:24]** mini nvim library. Like it says, there's
**[33:26]** more than 40 of these. So there might be
**[33:29]** more that you like the look of and that
**[33:31]** you might leverage. It even has its own
**[33:34]** status bar for example, even though
**[33:35]** we've created our own. And it has a
**[33:37]** completion engine, even though I'm going
**[33:39]** to be using Blink for the completion,
**[33:41]** but we'll get to that. Okay, the next
**[33:43]** thing is going to be Git Signs. This is
**[33:46]** a plugin which speaks for itself. It's
**[33:48]** git integration for our buffers and it's
**[33:50]** going to give us nice navigation to our
**[33:54]** different hunks and it's also going to
**[33:55]** give us visual feedback on the changes
**[33:58]** and the deletions and the additions in
**[34:00]** our code when it comes to opening files.
**[34:03]** We can immediately grasp what's changed
**[34:05]** and we can navigate to that. If I had to
**[34:07]** choose one Git plugin, then I'm going to
**[34:09]** choose this one. Although Git Fugitive
**[34:12]** is a fabulous plugin, but like I said,
**[34:14]** I'm down to 10. I just want to choose
**[34:16]** the 10 which are really really good for
**[34:18]** me and these are the ones that I've
**[34:20]** chosen. So we're installing it up here.
**[34:22]** Now we're adding it. Gets science.nv.
**[34:25]** And then down here I've got a lot of
**[34:27]** different settings. So I'm going to set
**[34:29]** it up. I'm going to add some signs. So
**[34:31]** an addition is a narrow line. Change is
**[34:33]** a thicker line. Deletion is a small
**[34:35]** circle. Top delete is a small circle.
**[34:38]** Change delete is a larger circle. And
**[34:41]** unttracked is just an empty circle. You
**[34:43]** can choose whatever kind of icons that
**[34:45]** you want, but I've got a few shortcuts
**[34:48]** here. So, for example, we go to the next
**[34:51]** hunk, the previous hunk, and we can
**[34:54]** reset them. Okay. And so, once we've got
**[34:57]** git sign set up, let's close everything.
**[35:00]** I'm going to go back in. It's going to
**[35:02]** ask us to install.
**[35:06]** Okay. And we can see that we've got some
**[35:11]** changes here. Here we've got some
**[35:12]** deletions. We've got some additions and
**[35:16]** so forth. Okay. And so if I want to go
**[35:17]** to the next hunk, I can simply say close
**[35:19]** square bracket H and it's going to take
**[35:21]** me to the next thing. I could preview it
**[35:24]** with
**[35:26]** leader HP and we can see what's changed.
**[35:30]** All right, pretty powerful. In your own
**[35:32]** time, go and have a look at the
**[35:33]** documentation for git signs here on the
**[35:35]** left. Okay, the next plugin and an
**[35:38]** important plugin is going to be NVM tree
**[35:42]** sitter. So tree sitter is the
**[35:46]** configuration, the abstraction and the
**[35:48]** passes so that nem properly understands
**[35:51]** your code. It's not just text. It can
**[35:53]** understand that things are certain
**[35:54]** objects. It understands declarations of
**[35:57]** objects, functions and the shape of the
**[36:00]** code that we're seeing on the screen. So
**[36:02]** it helps us to navigate. It helps it on
**[36:04]** the highlighting and it helps us on the
**[36:07]** formatting and everything. So, it's a
**[36:08]** very critical plugin and we're going to
**[36:11]** install it here. Now, one of the things
**[36:13]** about it is that recently the API
**[36:15]** changed and so I'm using the new main
**[36:18]** branch. When I say recently, it was
**[36:20]** probably about a year ago now, but a lot
**[36:22]** of people haven't got around to it. And
**[36:24]** if you go to their website, you can see
**[36:26]** that has caution. It says that this is
**[36:28]** an incompatible rewrite on the main
**[36:30]** branch. But if you want, you can still
**[36:33]** use the master one. So if you want, you
**[36:35]** can go ahead and use the master one. But
**[36:36]** in this one, I'm actually using the
**[36:38]** updated one. It requires nearm 11 or
**[36:41]** later. Of course, we've got that. And
**[36:44]** here it has the installation
**[36:45]** instructions. And we're going to install
**[36:47]** it here. And then once again, we're
**[36:49]** going to load it here. Now I've actually
**[36:51]** got a function that I've written for
**[36:54]** Creitter. And I've got a bunch of
**[36:56]** different passes. the passes being the
**[37:00]** way that nem or tree sitter installs
**[37:03]** these passes. So that the files whether
**[37:06]** they're vim or rust or c or javascript
**[37:08]** or whatever these are the ones that I
**[37:11]** want to be installed. The old syntax
**[37:13]** used to have an insure installed option.
**[37:16]** It doesn't have it anymore. And so what
**[37:17]** I've done is I've created this here in
**[37:19]** order to emulate the old behavior.
**[37:22]** Basically we're going to require tree
**[37:24]** sitter and then I've got a list of all
**[37:26]** these. We're going to set up tree sitter
**[37:28]** and then I've got a list here of all of
**[37:30]** the functions that I mainly use. You can
**[37:32]** add in more. You can remove some if you
**[37:34]** want. Then we're going to get the
**[37:37]** config. We're going to find out which of
**[37:39]** these passes, these language passes
**[37:41]** already installed. And then if any of
**[37:44]** them haven't been installed, then we
**[37:46]** want to install them. Okay. And then
**[37:49]** finally,
**[37:51]** if we have a look in here, we're going
**[37:53]** to based on the certain file type, we're
**[37:57]** going to load that passer. Last thing
**[37:59]** that we want to do is just call this
**[38:01]** function that I've declared above. All
**[38:02]** right, let's exit out.
**[38:08]** It's going to ask us to install.
**[38:11]** Okay. And so now we've got this ts
**[38:14]** command. All right. And we can say ts
**[38:18]** install. And we can also manually do it.
**[38:21]** So when you come in here, if you add any
**[38:23]** languages or you remove any languages,
**[38:25]** then you're going to find that they
**[38:26]** automatically get downloaded assuming
**[38:28]** that they're in that insure installed
**[38:30]** list. Trixit is going to become more
**[38:32]** apparent later. And it's helpful. You
**[38:35]** know earlier when we looked at the
**[38:37]** options for example if you didn't really
**[38:39]** want to see this or what we can say in
**[38:42]** near is ZC or Z C and that's going to
**[38:46]** close that and Z that opens it back up
**[38:50]** and so I can open and close these
**[38:53]** different groups and tree setter helps
**[38:55]** NEM to understand the syntax. All right
**[38:57]** in this next section we're going to
**[38:59]** cover language server protocols. No good
**[39:01]** NEVM setup. and a modern coding
**[39:03]** configuration setup is complete without
**[39:06]** language server protocols. So we're
**[39:08]** going to be leveraging invim LSP config.
**[39:11]** Basically this has out of the box
**[39:13]** sensible configurations for many many
**[39:16]** LSPs and I'm going to teach you how to
**[39:19]** set it up for Python and Lure and
**[39:21]** TypeScript and also C. I feel like every
**[39:25]** single configuration should have C in it
**[39:27]** and also Golang. But the point is that
**[39:30]** you're going to be able to set it up for
**[39:32]** more. And once you understand the
**[39:35]** pattern of what I impart here and how to
**[39:38]** set up your own language servers and
**[39:40]** also your llinters and formatterers from
**[39:42]** that point on you will be able to
**[39:44]** configure it to your personal liking. So
**[39:47]** NVM lspig that is one of the plugins
**[39:51]** that we need to add and also we're going
**[39:54]** to add in Mason. So here we've got nvm
**[39:56]** lssp config and then mason. What it is,
**[39:59]** it's a package manager that runs or
**[40:03]** allows you to install your language
**[40:06]** server protocols, your debug adapter
**[40:09]** protocols, llinters, and formatterers.
**[40:10]** And we're going to be using this to
**[40:12]** install the language servers for those
**[40:16]** languages that I just listed. In here
**[40:18]** under vim pack add, I've added the
**[40:20]** section for language server protocols or
**[40:23]** LSPs. And down here, I'm going to also
**[40:26]** include them
**[40:28]** here under pack ad because as we know,
**[40:30]** we need to load them. Now, going to move
**[40:33]** down here to the LSP section. The first
**[40:36]** thing that I want to do is I want to use
**[40:38]** the native Vim API, the diagnostics,
**[40:42]** just to set some better error or warning
**[40:46]** or hint or information info signs. So,
**[40:50]** I've added that here. And all this
**[40:53]** section of the code does is it just
**[40:55]** applies the these nice icons up here. Of
**[40:58]** course, you can edit those to your
**[41:00]** liking. And so when we get diagnostics,
**[41:03]** which is when we think about the
**[41:05]** benefits of the language server, we're
**[41:06]** getting definitions, diagnostics, we're
**[41:09]** getting a lot of stuff. And so these
**[41:11]** diagnostic signs are important just to
**[41:13]** show better feedback from the LSP. Now
**[41:16]** in this next section, I've got an LSP
**[41:19]** onattach function. So what does this do?
**[41:22]** Well, we can map based on the client
**[41:26]** that we're using. So for example, we
**[41:27]** might be using lure language server or
**[41:30]** we might be using TypeScript language
**[41:32]** server. Whatever it is, we can map
**[41:34]** certain shortcuts. So for example, I've
**[41:36]** got a bunch here and some of these
**[41:38]** leverage FCF lure that we installed
**[41:41]** earlier. So there's some basics like
**[41:44]** leader G and then capital D that means
**[41:46]** go to the definition. leader G and then
**[41:49]** S. That means go to the definition in a
**[41:51]** split on the side. I use vertical split
**[41:55]** by default. We can invoke code actions.
**[41:57]** We can re rename things. We can open up
**[42:01]** the diagnostics for the line or under
**[42:04]** the cursor. We can go to the next or the
**[42:06]** previous diagnostic. We can hover on the
**[42:08]** definition. And we can also invoke a
**[42:11]** bunch of stuff here. So for example,
**[42:14]** this one leader FD shows all of the file
**[42:16]** definitions and then leader FR is all
**[42:20]** the references
**[42:22]** and we've got type definitions, document
**[42:25]** symbols for all the symbols, function
**[42:27]** declarations and that kind of thing.
**[42:29]** Workplace symbols, LSP implementations.
**[42:33]** So the last section under the on on
**[42:35]** attach is if our language server client
**[42:38]** supports
**[42:40]** organized imports. So for example,
**[42:42]** Python or whatever we want to organize
**[42:45]** our imports at the top of our file, then
**[42:47]** leader OI will allow us to organize
**[42:50]** those imports. Down here, we've got
**[42:52]** another auto command. I'm not going to
**[42:53]** put this under the auto command section
**[42:55]** because I think that it is so pertinent
**[42:58]** to this section. I don't want to confuse
**[43:00]** things. And so just under the onattach
**[43:02]** function, when there's an LSP attach
**[43:04]** event, then we want to add this LSP
**[43:09]** onattach function
**[43:11]** here,
**[43:12]** which we just declared and we just had a
**[43:15]** look at. We want to add that to the
**[43:16]** callback so that this gets attached
**[43:19]** anytime a language server is attached.
**[43:21]** We're going to have all of those
**[43:23]** shortcuts available. Few more key maps
**[43:25]** that I'm going to set. For example,
**[43:26]** leader Q. That is going to open up the
**[43:29]** diagnostics list and then leader DL is
**[43:33]** going to open up the line diagnostics.
**[43:35]** Okay, that's all well and good. We've
**[43:37]** added Mason above. Right now, the last
**[43:40]** thing that we need to do is we actually
**[43:42]** need to
**[43:44]** call Vim LSP config. And so these are
**[43:48]** the language servers that I'm going to
**[43:50]** set up here with lure ls, pyrite for
**[43:52]** python, bashls for obviously bash shell
**[43:56]** scripting, tsls for the typescript
**[44:00]** language server, go pls
**[44:03]** and c langd. So we need to make sure
**[44:06]** that we've installed all of these
**[44:08]** language servers. We do that using mason
**[44:10]** that we just looked at. So what I'm
**[44:11]** going to do, I'm going to
**[44:14]** exit out. When we come back in, it's
**[44:16]** going to ask us if we want to install
**[44:18]** those plugins. We're going to go ahead
**[44:21]** and say yes. Okay. And so once they've
**[44:23]** installed, come back in and just make
**[44:25]** sure that you also just under where we
**[44:27]** were doing the git signs or wherever is
**[44:29]** appropriate for you, we need to require
**[44:31]** Mason because we've installed it, but we
**[44:34]** need to make sure that it's available
**[44:35]** for us to use. And therefore, I'm going
**[44:38]** to go and now I'm going to invoke Mason.
**[44:42]** And what's going to happen here, it's
**[44:43]** going to go and look up a list of all
**[44:45]** the language servers, llinters, and
**[44:47]** formatterers. And we're starting with
**[44:48]** the LSPs. So the first thing I'm going
**[44:50]** to do, I'm going to use forward slash
**[44:52]** and I'm going to search for lure and
**[44:54]** lure language server. And then once I
**[44:56]** found it, I'm just going to hit I. And
**[44:58]** what that's going to do is that's going
**[45:00]** to install it. So we see it's
**[45:02]** installing. Okay. And so L has been
**[45:04]** installed. And now let's go into Pyrite.
**[45:07]** And then I'm going to install the
**[45:08]** TypeScript language server, clang, the
**[45:11]** bash language server, and finally go pls
**[45:14]** for the go language server. Okay, so
**[45:17]** just make sure that they're all
**[45:18]** installed. Okay, so we've installed
**[45:20]** those language servers. But language
**[45:22]** servers are well complemented by
**[45:24]** llinters and formatterers. And for
**[45:27]** linting and formatting, what I'm going
**[45:29]** to be doing is I'm going to be using a
**[45:30]** thing called EFM lang server. So EFM is
**[45:34]** what we call a general purpose language
**[45:37]** server. So we can plug in all of our
**[45:39]** llinters and formatterers into this
**[45:41]** general purpose language server and it's
**[45:43]** going to give us the ability to lint and
**[45:46]** format the code. Now it's got out of the
**[45:48]** box plugins. And so the first thing I'm
**[45:51]** going to do here is I'm going to add
**[45:53]** this plugin which is efm lsconfigs env.
**[45:58]** Okay. Okay. And so I've added the URL
**[46:00]** here to install. And under pack ad,
**[46:04]** under pack ad, we're just going to say
**[46:06]** pack efmls
**[46:09]** configs
**[46:10]** env. Okay. And now down the bottom where
**[46:13]** we were setting up our language servers.
**[46:15]** We're going to use in the case for
**[46:16]** example of lure, we're going to have
**[46:18]** lure check for our linting and star lure
**[46:21]** for the formatting. For Python, we're
**[46:22]** going to have flake 8 and black. So
**[46:24]** black's the formatter, flake 8 is the
**[46:27]** llinter. And then we're going to use
**[46:28]** prettier. Pritier is pretty powerful.
**[46:30]** You can apply it for not just
**[46:31]** JavaScript, but also CSS and JSON and
**[46:34]** stuff like that. So I'm actually going
**[46:36]** to include it there. ESLint as well.
**[46:39]** Then we got prettier. Prettier is
**[46:41]** applicable to many different types of,
**[46:44]** you know, web languages. So I'm going to
**[46:46]** include that as the formatter. And then
**[46:49]** ESLint is also pretty adaptive. I'm
**[46:52]** going to put that for the llinters.
**[46:54]** We're going to apply each of these in a
**[46:55]** moment. JSON we're going to have a
**[46:57]** formatter fix JSON and then for our bash
**[47:00]** we're going to have shell check for the
**[47:02]** llinter and shmt for the formatter and
**[47:06]** then for C and C like languages we're
**[47:10]** going to be using CPP lint C++ lint and
**[47:13]** then C lang format for the formatter. So
**[47:16]** I've got all of these languages here or
**[47:19]** these file types and underneath this. So
**[47:22]** you got to stipulate to the EFM language
**[47:24]** server that these are the file types
**[47:26]** that we want to have linting and
**[47:28]** formatting for and then you need to pass
**[47:31]** in what are the specific formatterers
**[47:34]** and lintters for each. So for example C
**[47:37]** we've got lang format. Same thing for
**[47:40]** C++. All right, CSS we're going to use
**[47:42]** prettier and same with HTML. And then
**[47:45]** JavaScript, JavaScript, React,
**[47:47]** TypeScript, TypeScript, React. They're
**[47:49]** all going to leverage ESLint and
**[47:51]** prettier. The same thing goes for Vue
**[47:53]** Lure. Of course, we're going to use Lure
**[47:55]** Cheek and Python. We're going to have
**[47:57]** Flake 8 and Black. So before we can do
**[48:00]** anything here though, we need to firstly
**[48:03]** we're going to enable the EFM language
**[48:05]** server cuz this is the general language
**[48:07]** server that we're using here. And on top
**[48:10]** of that, we need to install all of these
**[48:13]** formatterers and llinters. So, let's go
**[48:15]** and do that. We can use Mason once again
**[48:18]** and we can go over to llinters and let's
**[48:21]** just go and install them. So, we got
**[48:23]** flake 8 lure check. And in the case of
**[48:26]** lure check, it's saying that we don't
**[48:28]** have lure rocks in our path. So, let's
**[48:31]** exit out.
**[48:34]** Okay. So, I'm on an arch system, right?
**[48:37]** So, I'm going to be installing lure
**[48:39]** rocks just using Pac-Man.
**[48:41]** All right, once it's installed, let's go
**[48:43]** back into our config. We can install the
**[48:46]** efm ls configs and let's return to mason
**[48:50]** and under the llinters. I'm going to
**[48:52]** look for lure again. So, we got lure
**[48:54]** check. I'm going to install that. Now,
**[48:56]** I'm going to look for bash using shell
**[49:00]** check. For C and C++ languages, I'm
**[49:02]** going to use CPP lint. I'm going to be
**[49:04]** using eslint D for TypeScript,
**[49:08]** JavaScript, but also all those other
**[49:09]** languages that we talked about. Okay.
**[49:11]** And I just realized that I had neglected
**[49:14]** to include Go, which is one of the
**[49:16]** demonstration languages. So for the
**[49:17]** llinter, we're going to use Go Revive.
**[49:19]** And for the formatter, we're going to
**[49:21]** use Go FT. So let's go and install first
**[49:25]** the Llinter. Okay. And so we've got
**[49:28]** these llinters now installed. And let's
**[49:31]** go and install the required
**[49:33]** formatterers. So in the case of Python I
**[49:36]** was using black. In the case of bluer I
**[49:39]** was using stylure. In the case of go I'm
**[49:41]** using go f u m pt. In the case of shell
**[49:45]** I'm using sh fmt json fix json. Finally
**[49:51]** prettier d. All right. So once you've
**[49:53]** got all of these formatters and llinters
**[49:56]** and this is obviously if you were using
**[49:59]** another language this is a good point
**[50:02]** where you can kind of understand the
**[50:05]** pattern here and you can go ahead and
**[50:08]** install any of the languages that you
**[50:11]** want here. Okay. And so so for example
**[50:14]** if you were using Ruby then you could
**[50:17]** come down and install the Ruby formatter
**[50:19]** and the same thing goes for the language
**[50:20]** server and the llinter. Okay team, we're
**[50:23]** getting pretty close here. And so the
**[50:26]** last thing that we need to do before we
**[50:27]** can test all of these lentters and
**[50:29]** formatterers, recall earlier that we set
**[50:32]** efm here to enable. Now what we need to
**[50:36]** do, this is the last time we need to
**[50:38]** open up Mason. And under our LSPs, we
**[50:41]** also need to install EFM.
**[50:44]** EFM doesn't have any keywords, but
**[50:46]** that's the general purpose language
**[50:48]** server. Going to install it. Now, in
**[50:50]** order to get it to work, you will need
**[50:52]** to have Go installed on your system. So,
**[50:54]** just make sure that you do that. Okay.
**[50:56]** And now what I'm going to do, I'm going
**[50:58]** to write and close. We just installed
**[51:00]** EFM. I'm going to open up my init.lure.
**[51:05]** And in here, we're going to start to see
**[51:07]** some lure check feedback. And
**[51:11]** specifically, what it's saying is that
**[51:14]** we've got this global variable Vim. lure
**[51:17]** check doesn't know what it is and we're
**[51:19]** mutating it. So, what we need to do, I'm
**[51:21]** going to open up the file explorer and
**[51:23]** in here I've got a lure check RC. I'm
**[51:26]** going to hit R and I'm going to change
**[51:28]** that to activate it. I previously
**[51:30]** prefixed it with back just so it wasn't
**[51:32]** on. All this has is a global vim and I'm
**[51:36]** going to do the same thing in this lure
**[51:38]** rc.json. These are the lure language
**[51:41]** server settings. So we see here we've
**[51:45]** got another diagnostics globals and
**[51:48]** that's vim. So now let's go back to our
**[51:52]** init and we're going to restart.
**[51:54]** Okay. And so I'm back in and we've got
**[51:56]** those settings for the global vim and
**[51:59]** that means it's not giving us any
**[52:00]** warnings. But if I say leader nd we can
**[52:04]** see here and I'm going to set wrap just
**[52:06]** so that we can see this entire line. We
**[52:08]** can see that lure check is giving us
**[52:10]** feedback on this because this line is
**[52:11]** too long. it's more than 120 characters,
**[52:14]** which must be the default in lower
**[52:15]** check. And just for some basic checks,
**[52:19]** for example, if I make it so the syntax
**[52:22]** isn't valid, it's going to say that
**[52:24]** we're missing a symbol. So, I'm going to
**[52:26]** put that symbol back. Finally, if we go
**[52:29]** to our auto commands, I've added a
**[52:32]** format on save. So, for example, before
**[52:35]** we write to the buffer on this hook,
**[52:37]** which is buff write pre. So, right
**[52:40]** before we write to the buffer, any of
**[52:42]** these files with a suffix listed here,
**[52:46]** we're going to check if there is a
**[52:48]** client, an EFm client attached, and
**[52:50]** we're going to use EFM to format the
**[52:52]** file. So, let's just say that I go in
**[52:54]** here and I mess around with some of the
**[52:58]** formatting.
**[53:00]** When I write, it's going to format.
**[53:02]** Okay, we're getting pretty close. But
**[53:04]** the thing is the last thing that I want
**[53:07]** to do is I want to introduce blink.cmp.
**[53:11]** Okay. So blink.cmp
**[53:13]** is a performant batteries included
**[53:16]** completion plugin for neoven. What does
**[53:18]** that mean? It is going to help us to
**[53:20]** reference our language servers, our
**[53:22]** buffers, our path and also a snippet
**[53:26]** engine to get those VS code like
**[53:29]** snippets. So this is called L snip and
**[53:32]** this has got a bunch of snippets written
**[53:35]** in Lua available for NEM. And so we're
**[53:38]** going to be having completion because
**[53:40]** obviously that's one of the most
**[53:41]** powerful things that we would have in
**[53:43]** any kind of modern editing environment.
**[53:46]** In here I've added blink cm which are
**[53:49]** obviously the
**[53:52]** URL. I needed to add the version and
**[53:54]** then down below that I've also added
**[53:56]** Lewis snip. So, we're going to install
**[53:58]** those and then make sure that once
**[54:00]** you've installed, you also are going to
**[54:02]** be calling pack ad. Now, let's go and
**[54:05]** have a look at Blink's setup. Blink. I'm
**[54:09]** going to put it under the same section
**[54:11]** with respect to
**[54:14]** our LSP. So, let's say this is LSP.
**[54:17]** It's not really just LSP anymore, but
**[54:19]** we're going to say it's linting,
**[54:22]** formatting,
**[54:26]** and completion.
**[54:32]** Okay, so just walking through the setup
**[54:34]** though, we've got some key mats. So
**[54:36]** basically, we got control and space to
**[54:39]** show or hide the completion options. And
**[54:41]** then we also have enter to accept. So
**[54:45]** carriage return stands for enter here.
**[54:47]** Control J and K just means that we can
**[54:50]** go to the next or the previous
**[54:52]** completion option that's being presented
**[54:54]** to us and tab and shift tab to look at
**[54:57]** the next or the previous snippet. Now
**[55:00]** this important part here is that we've
**[55:03]** got some sources. As I mentioned, one of
**[55:05]** the most powerful things about language
**[55:07]** server protocols is that we can use them
**[55:09]** for the definitions and also to look at
**[55:11]** the function signatures and look at the
**[55:13]** completion options. We've got the path
**[55:16]** that just refers to where we are
**[55:18]** relative to other files. And our buffer,
**[55:21]** so all of our open buffers, it's going
**[55:23]** to be able to have a look at that, see
**[55:24]** any of the symbols that are attached and
**[55:27]** that kind of thing. And finally,
**[55:28]** snippets. So, as I mentioned a moment
**[55:30]** ago, we're going to be using Lewis Snip.
**[55:32]** And Lewis Snip is this plug-in engine
**[55:36]** written for Neovm. So we're going to
**[55:39]** tell Blink our completion plugin, please
**[55:42]** use Lewis Snip, which is installed. Now
**[55:45]** it has fuzzy finding capabilities. And
**[55:47]** in order to get that working, I had to
**[55:49]** set download to true on the pre-built
**[55:52]** binaries.
**[55:54]** Finally, once we've got Blink completely
**[55:56]** set up, we want to say on the LSP config
**[55:59]** for every single one of these language
**[56:02]** servers. So, you see down below we've
**[56:04]** got Lure, Pyite, all those ones that
**[56:06]** we've been working on. Well, we want to
**[56:08]** say please attach the completion
**[56:11]** capabilities to all of the language
**[56:13]** servers so that we get even if we don't
**[56:15]** have a language server installed, we
**[56:17]** would still get some capabilities. You
**[56:19]** can imagine things like the buffer and
**[56:22]** the path and that kind of thing.
**[56:23]** Excellent. So, we are set up and now
**[56:27]** we're ready to demonstrate what this
**[56:28]** looks like. Okay. So, now I've got a
**[56:31]** very simple Python file. It's just got
**[56:34]** this test function and I just want to
**[56:36]** demonstrate some of the aspects. So, for
**[56:40]** example, let's say I wanted to import
**[56:42]** let's say I wanted to import. Well, we
**[56:44]** can say s add. We see everything that we
**[56:47]** can import now with our completion. And
**[56:49]** if we come down here, we can say sys and
**[56:53]** maybe we want to get see if there's
**[56:57]** anything with version. There is there's
**[56:58]** version info. All right. Okay. It's
**[57:01]** actually not callable. It's telling us
**[57:02]** the L LSP is giving us that information.
**[57:05]** Flake 8, the llinter is telling us,
**[57:07]** okay, it is it or it requires or expects
**[57:10]** two lines. We didn't actually have to do
**[57:11]** that manually because we can write and
**[57:14]** it's got a going to auto format pretty
**[57:16]** good. So this is set up for all those
**[57:18]** languages that we discussed. Now in this
**[57:20]** section we're getting close to the end.
**[57:22]** I often let's say we want to use a
**[57:25]** terminal. Well, what we could do in the
**[57:27]** event is we could do Ctrl Z. That puts
**[57:30]** it into the background and then we could
**[57:31]** bring it to the foreground with FG.
**[57:33]** However, what I've got here is I've got
**[57:35]** a floating terminal. So basically what
**[57:37]** we're going to be doing is setting up a
**[57:39]** few auto commands so that we create a
**[57:41]** buffer for the terminal and we want to
**[57:44]** do things like we want to turn off the
**[57:45]** numbers the relative numbers and we
**[57:47]** don't want a sign column when we've got
**[57:48]** a terminal open and this is a function
**[57:51]** which creates the floating terminal. So
**[57:53]** for example it puts it on 80% of the
**[57:56]** height and 80% of the width and it's got
**[57:59]** a few styling components and a few
**[58:02]** highlight components. And so basically
**[58:06]** this section all it's doing is it's just
**[58:08]** setting up a floating terminal. This is
**[58:10]** totally up to you. You can use plugins
**[58:13]** but we've actually hit our maximum of 10
**[58:15]** plugins now. Now if we wanted to invoke
**[58:17]** this we can use leader t or we can hit
**[58:20]** escape to close it. So let's restart.
**[58:25]** And so now what I'm going to do I'm
**[58:26]** going to hit leader t and we've got a
**[58:29]** terminal and see print working
**[58:32]** directory. We've got that. If we hit
**[58:33]** escape, it goes away. If we hit it
**[58:35]** again, it's back and it persists. Okay.
**[58:37]** So, right at the beginning, we set our
**[58:40]** theme. And the last thing I'm going to
**[58:42]** do is I'm going to include this set
**[58:45]** transparency
**[58:46]** function. So, all this does is it gets
**[58:49]** all the elements and it makes them
**[58:51]** transparent because I think that's a
**[58:52]** nice thing in your configuration to have
**[58:55]** transparency.
**[58:57]** And under NVM tree, I'm also going to
**[58:59]** apply these options just to make sure
**[59:01]** that it's fully transparent. So let's
**[59:03]** let's restart.
**[59:05]** And you're going to see that it's
**[59:07]** actually not transparent yet. And that's
**[59:09]** because my terminal emulator I'm using
**[59:12]** Kitty and it itself is not transparent.
**[59:15]** So go to your respective terminal
**[59:18]** emulator. I'm going to go into here and
**[59:20]** I'm going to change the background
**[59:22]** opacity to 0.8.
**[59:26]** And now we can see that we've got
**[59:28]** transparency
**[59:30]** and
**[59:32]** our configuration is complete. Okay. And
**[59:36]** just to wrap up, I wanted to touch on
**[59:38]** some honorable mentions of other plugins
**[59:40]** that I've used because we've limited
**[59:43]** ourselves to 10, but you can actually
**[59:45]** add in more. And you know, these are
**[59:47]** excellent plugins that I've used in the
**[59:49]** past myself. So for example, Kodium by
**[59:52]** Windsurf is a great AI completion
**[59:55]** plugin. We also have LSP saga. What this
**[59:57]** one does is it makes your LSP experience
**[1:00:00]** even nicer with better UI and nice nice
**[1:00:04]** shortcuts. Lure line. Now we built our
**[1:00:07]** own status line, but you can use Line if
**[1:00:09]** you'd like. It's a really really great
**[1:00:12]** status line. NVM DAP UI is for the
**[1:00:15]** debugger adapter protocol. Now, we
**[1:00:17]** didn't use that in this configuration.
**[1:00:19]** And frankly, I don't really use the
**[1:00:20]** debugger that much, but this is an
**[1:00:22]** excellent plugin if you'd like to use
**[1:00:24]** that. Rustation is for Rust and it's a
**[1:00:27]** supercharged Rust experience for Neoim.
**[1:00:29]** If you do code in Rust, then I'd highly
**[1:00:31]** recommend this rather than going through
**[1:00:33]** the path that we went today. This
**[1:00:35]** plug-in takes care of all the LSP, the
**[1:00:37]** linting, formatting, and so forth.
**[1:00:39]** Trouble Envim is a diagnostics plugin.
**[1:00:43]** It's excellent for workplace diagnostics
**[1:00:45]** and getting a feel for the references
**[1:00:48]** and telescope results, quick fix and
**[1:00:50]** that kind of thing. Vim Fugitive, it's a
**[1:00:52]** Git wrapper. I use the terminal most of
**[1:00:55]** the time to do my Git work and so I
**[1:00:57]** didn't include this plugin, but if you
**[1:00:58]** want to have a great Git wrapper, this
**[1:01:01]** is the one. Now, especially for
**[1:01:03]** newcomers, when you get into NEM, some
**[1:01:07]** of the key binds, they don't really
**[1:01:08]** stick. So, which key? It basically just
**[1:01:10]** gives you you hit the leader key space
**[1:01:13]** in our configuration today and then it
**[1:01:16]** tells you all of the associated
**[1:01:19]** keybinds that you can use. So this is
**[1:01:20]** great for learning your keybinds and
**[1:01:22]** understanding what keybinds are
**[1:01:23]** available. Finally, if you do a lot of
**[1:01:25]** writing or coding, you want
**[1:01:28]** distractionfree, then I think Zen mode
**[1:01:30]** is an excellent plugin and I use this
**[1:01:32]** one a lot myself. It basically just
**[1:01:34]** simplifies the whole UI. It cleans
**[1:01:37]** everything up. It's a really nice
**[1:01:38]** plugin. Well, congratulations. You've
**[1:01:41]** come this far. You've got your own
**[1:01:43]** custom Neoim configuration in less than
**[1:01:46]** a thousand lines. You've got 10 plugins
**[1:01:49]** which you can build on because you know
**[1:01:50]** enough about the built-in plug-in
**[1:01:52]** manager to be dangerous. And you're
**[1:01:55]** becoming a little bit of a Vim
**[1:01:57]** connoisseur. So, if you enjoyed this
**[1:02:00]** video, if you'd like to see more videos
**[1:02:02]** like this, please do subscribe. means a
**[1:02:05]** lot that you joined today and I hope to
**[1:02:08]** see you in the next one.
**[1:02:10]** Thank you.
