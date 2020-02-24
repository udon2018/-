#!/usr/bin/env python3
#! -*- coding:utf-8 -*-

import discord
import random

client = discord.Client()
text_channel = 315744357049303042  #じぇねらるのid
my_id =   #自分のid
token =
text_chat = None
@client.event
async def on_ready():
	global text_chat = get_channel(text_channel)
	print ('Logged in as')
	print (client.user.name)
	print (client.user.id)
	print ('------')
	await client.change_presence(activity=discord.Game("うどネット"))
	msg1 = ["守り神、ただいま着任いたしました。優しく微笑みますよっっ！", "寒いですね・・・", "私は帰ってきました！", "チョコが待ち遠しい！"]
	msg = random.choice(msg1)
	channel = taxt_chat
	await channel.send(msg1)

@client.event
async def on_member_join(member):
	await member.send('ようこそ、Planetside2 UDONサーバーへ！！サーバーに参加するにあたり、読んでねチャンネルを一読ください')

@client.event
async def on_message(message):
	if message.content.startswith("ただいま"):
	    if client.user != message.author:
	    	m = "おかえりなさい" + message.author.name + "さん"
	    await message.channel.(m)

	elif message.content.startswith("おやすみ"):
	    if client.user != message.author:
        	n = "おやすみなさいませ" + message.author.name + "さん"
	        await message.channel.(n)


	elif message.content.startswith("あへ"):
	    if client.user != message.author:
        	o = "✌(´◓ｑ◔｀)✌" + message.author.name + "さん"
	        await message.channel.(o)


	elif message.content.startswith("おはよう"):
	    if client.user != message.author:
        	p = "おはようございます" + message.author.name + "さん"
	        await message.channel.(p)


	elif message.content.startswith("おちます"):
	    if client.user != message.author:
        	q = "いってらっしゃい" + message.author.name + "さん"
	        await message.channel.(q)


	elif message.content.startswith("こんにち"):
	    if client.user != message.author:
        	r = "こんにちは" + message.author.name + "さん"
	        await message.channel.(r)


	elif message.content.startswith("VS"):
	    if client.user != message.author:
        	s = ["ヴぁぬー", "Papa Vanuはあなたを見守っています", "Vanuはあなたに微笑みかけます", "その兵士、紫の力を纏いて・・・"]
	        s2 = random.choice(s)
        	await message.channel.(s2)


	elif message.content.startswith("お茶"):
	    if client.user != message.author:
        	t = ["( ^-^)_旦", "(*^ｰ)_旦~~ｵﾁｬﾊｲｶｶﾞ?", "\お茶でも ( ^-^)o旦~~ どぞ ♪ > 皆の衆", "―＝三(*^ー)_旦~~ ﾍｲ! ｱｶﾞﾘｲｯﾁｮｳ!!", "ﾏｧﾏｧ､ｵﾋﾄﾂ(*￣ー￣)_凸", "ｵﾁｬﾄﾞｿﾞ ( ﾟдﾟ)_旦~)`νﾟ)･;'ｱﾁﾁ!!", "( ^-)_旦~~ ﾊｲ､ｻﾞﾊﾞｰ(;･_･)/◇⌒ﾐﾐﾐ ｼﾏｯﾀ!", "(* ^^)ノ±■　コーヒー飲む？"]
	        t2 = random.choice(t)
        	await message.channel.(t2)


	elif message.content.startswith("眠い"):
	    if client.user != message.author:
        	u = ["起きてぇぇぇ！！！！", "布団、用意しましたよ♡", "ｽﾔｧｧ・・・", "そろそろ寝ましょう！", "(=_ヾ) ﾈﾑﾈﾑｩ", "(ρ_･).｡o○ねみゅいのｰ･･", "Ｚｚｚ (￣～￣) （マス・・タァ・・）"]
	        u2 = random.choice(u)
        	await message.channel.(u2)


	elif message.content.startswith("はっくし"):
	    if client.user != message.author:
        	v = ["あらあら大丈夫ですか？ハンカチどうぞ～", "くしゅん・・・移っちゃいました///", "寒い・・・ですか？", "体調にお気をつけてくださいね！"]
	        v2 = random.choice(v)
        	await message.channel.(v2)

client.run('token')

