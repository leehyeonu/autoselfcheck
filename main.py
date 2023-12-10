import discord, asyncio, sqlite3, os
from hcskr.hcskr import asyncSelfCheck, asyncChangePassword, asyncUserLogin
import time

client = discord.Client()


@client.event
async def on_ready():
    print(f"Login: {client.user}\nInvite Link: https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot")
    while True:
        await client.change_presence(activity=discord.Game(f"자동자가진단 | {len(client.guilds)}서버 사용중"),status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game(f"Supporter : ! ! [Live]#7777"),status=discord.Status.online)
        await asyncio.sleep(5)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("!가입"):
            con = sqlite3.connect("./database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE id == ?", (message.author.id,))
            result = cur.fetchone()
            if not (result != None):
                cur.execute("INSERT INTO users Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (message.author.id, message.guild.id, "", "", "", "", "", "", "", ""))
                con.commit()
                con.close()
                await message.channel.send(embed=discord.Embed(title="가입 성공", description="성공적으로 가입되었습니다.", color=0x5c6cdf))
            else:
                return await message.channel.send(embed=discord.Embed(title="가입 실패", description="이미 가입되어있습니다.", color=0x5c6cdf))

    if message.content == "!정보등록":
        con = sqlite3.connect("./database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE id == ?", (message.author.id,))
        info = cur.fetchone()
        con.close()
        if not (info != None):
            return await message.channel.send(embed=discord.Embed(title="정보 등록 실패", description="가입되어있지 않습니다.\n!가입을 입력해주세요.", color=0x5c6cdf))
        else:
            await message.channel.send(embed=discord.Embed(title="자가 진단 신청 성공", description="디엠을 확인해주세요.", color=0x5c6cdf))
            def check(s):
                return (isinstance(s.channel,discord.channel.DMChannel) and (message.author.id == s.author.id))
            await message.author.send(embed=discord.Embed(title="자가 진단 정보 등록", description="본인이 거주중인 시 / 도 를 입력해주세요( ex | 서울, 경기, 전남, 전북).", color=0x5c6cdf))
            s = await client.wait_for('message', timeout=60, check=check)
            s1 = s.content
            print(s1)
            def check(ss):
                return (isinstance(ss.channel,discord.channel.DMChannel) and (message.author.id == ss.author.id))
            await message.author.send(embed=discord.Embed(title="자가 진단 정보 등록", description="본인이 재학중인 학급을 입력해주세요(ex | 유치원, 초등학교, 중학교, 고등학교 )", color=0x5c6cdf))
            ss = await client.wait_for('message', timeout=60, check=check)
            s2 = ss.content
            print(s2)
            def check(school):
                return (isinstance(school.channel,discord.channel.DMChannel) and (message.author.id == school.author.id))
            await message.author.send(embed=discord.Embed(title="자가 진단 정보 등록", description="학교명을 입력해주세요.", color=0x5c6cdf))
            school = await client.wait_for('message', timeout=60, check=check)
            schoolname = school.content
            print(schoolname)
            def check(name):
                return (isinstance(name.channel,discord.channel.DMChannel) and (message.author.id == name.author.id))
            await message.author.send(embed=discord.Embed(title="자가 진단 정보 등록", description="이름을 입력해주세요.", color=0x5c6cdf))
            name = await client.wait_for('message', timeout=60, check=check)
            names = name.content
            print(names)
            def check(br):
                return (isinstance(br.channel,discord.channel.DMChannel) and (message.author.id == br.author.id))
            await message.author.send(embed=discord.Embed(title="자가 진단 정보 등록", description="생년월일 6자리를 입력해주세요. ( ex | 001234 )", color=0x5c6cdf))
            br = await client.wait_for('message', timeout=60, check=check)
            brs = br.content
            print(brs)
            def check(p):
                return (isinstance(p.channel,discord.channel.DMChannel) and (message.author.id == p.author.id))
            await message.author.send(embed=discord.Embed(title="자가 진단 정보 등록", description="비밀번호를 입력해주세요. ( ex | 1234 )", color=0x5c6cdf))
            p = await client.wait_for('message', timeout=60, check=check)
            pw = p.content
            print(pw)
            print(s1, s2, schoolname, names, brs, pw, message.author)
            con = sqlite3.connect("./database.db")
            cur = con.cursor()
            cur.execute("UPDATE users SET sido = ?, rank = ?, school = ?, name = ?, birth = ?, password = ?, auto = ?, tags = ? WHERE id == ?;", (s1, s2, schoolname, names, brs, pw, 'X', f"{message.author}", message.author.id))
            con.commit()
            con.close()
            await message.author.send(embed=discord.Embed(title="정보 등록 성공", description="정보 등록이 성공적으로 완료되었습니다.\n!진단 명령어만 입력하시면 자동으로 자가진단이 완료됩니다.", color=0x5c6cdf))


    if message.content == "!진단":
        con = sqlite3.connect("./database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE id == ?", (message.author.id,))
        info = cur.fetchone()
        con.close()
        if not (info != None):
            return await message.channel.send(embed=discord.Embed(title="정보 등록 실패", description="가입되어있지 않습니다.\n!가입을 입력해주세요.", color=0x5c6cdf))
        else:
            try:
                await message.channel.send(embed=discord.Embed(title="디엠 성공", description="디엠을 확인해주세요.", color=0x5c6cdf))
                con = sqlite3.connect("./database.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM users WHERE id == ?", (message.author.id,))
                info = cur.fetchone()
                con.close()
                s1 = info[2]
                s2 = info[3]
                schoolname = info[4]
                names = info[5]
                brs = info[6]
                pw = info[7]
                ing = await message.author.send(embed=discord.Embed(title="자가 진단 진행중..", description="잠시만 기다려주세요.. 자가진단을 하는중이에요!", color=0x5c6cdf))

                hcskr_result = await asyncSelfCheck(names, brs, s1, schoolname, s2, pw)
                if hcskr_result['code'] == 'SUCCESS':
                    await ing.edit(embed=discord.Embed(title="자가 진단 성공 !", description=f"자가진단이 완료되었습니다!\n완료시각: {hcskr_result['regtime']}", color=0x5c6cdf))
                else:
                    await ing.edit(embed=discord.Embed(title="자가 진단 실패", description=f"자가진단이 실패했습니다\n사유: {hcskr_result['message']}", color=0x5c6cdf))
            except:
                await ing.delete()
                await message.author.send(embed=discord.Embed(title="자가 진단 실패", description="입력하신 정보가 일치하지 않거나 자가진단 도중 오류가 발생하였습니다.", color=0x5c6cdf))

    if message.content == "!비번변경":
        con = sqlite3.connect("./database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE id == ?", (message.author.id,))
        info = cur.fetchone()
        con.close()
        if not (info != None):
            return await message.channel.send(embed=discord.Embed(title="정보 등록 실패", description="가입되어있지 않습니다.\n!가입을 입력해주세요.", color=0x5c6cdf))
        else:
            await message.channel.send(embed=discord.Embed(title="디엠 성공", description="디엠을 확인해주세요.", color=0x5c6cdf))
            con = sqlite3.connect("./database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE id == ?", (message.author.id,))
            info = cur.fetchone()
            con.close()
            s1 = info[2]
            s2 = info[3]
            schoolname = info[4]
            names = info[5]
            brs = info[6]
            pw = info[7]
            def check(p):
                return (isinstance(p.channel,discord.channel.DMChannel) and (message.author.id == p.author.id))
            await message.author.send(embed=discord.Embed(title="자가 진단 정보 등록", description="새로운 비밀번호를 입력해주세요. ( ex | 1234 )", color=0x5c6cdf))
            p = await client.wait_for('message', timeout=60, check=check)
            npw = p.content
            print("비번 변경 LOG : " + npw, message.author)


            hcskr_result = await asyncChangePassword(names, brs, s1, schoolname, s2, pw, npw)
            if hcskr_result['code'] == 'SUCCESS':
                con = sqlite3.connect("./database.db")
                cur = con.cursor()
                cur.execute("UPDATE users SET password = ? WHERE id == ?;", (npw, message.author.id))
                con.commit()
                con.close()
                await message.author.send(embed=discord.Embed(title="비번 변경 성공!", description=f"비밀번호 변경이 완료되었습니다!\n변경한 비번 : {npw}", color=0x5c6cdf))
            else:
                await message.author.send(embed=discord.Embed(title="비번 변경 실패", description=f"비밀번호 변경이 실패했습니다\n사유: {hcskr_result['message']}", color=0x5c6cdf))

    #if message.content == "!예약":
        con = sqlite3.connect("./database.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE id == ?", (message.author.id,))
        info = cur.fetchone()
        con.close()
        if not (info != None):
            return await message.channel.send(embed=discord.Embed(title="정보 등록 실패", description="가입되어있지 않습니다.\n!가입을 입력해주세요.", color=0x5c6cdf))
        else:
            await message.channel.send(embed=discord.Embed(title="디엠 성공", description="디엠을 확인해주세요.", color=0x5c6cdf))
            def check(auto):
                return (isinstance(auto.channel,discord.channel.DMChannel) and (message.author.id == auto.author.id))
            ing = await message.author.send(embed=discord.Embed(title="자가 진단 정보 등록", description="새로운 비밀번호를 입력해주세요. ( ex | 1234 )", color=0x5c6cdf))
            auto = await client.wait_for('message', timeout=60, check=check)
            at = auto.content
            if at in ['x','X','False']:
                con = sqlite3.connect("./database.db")
                cur = con.cursor()
                cur.execute("UPDATE users SET auto = ? WHERE id == ?;", ("X", message.author.id))
                con.commit()
                con.close()
                await message.author.send(embed=discord.Embed(title="예약 해지 성공!", description="이제부터 자동 자가진단이 종료됩니다.", color=0x5c6cdf))
            if at in ['o','O','True']:
                con = sqlite3.connect("./database.db")
                cur = con.cursor()
                cur.execute("UPDATE users SET auto = ? WHERE id == ?;", ("O", message.author.id))
                con.commit()
                con.close()
                await message.author.send(embed=discord.Embed(title="예약 성공!", description="이제부터 자가진단이 매일 오전 7시에 진행됩니다", color=0x5c6cdf))

client.run("TOKEN") #봇토큰
