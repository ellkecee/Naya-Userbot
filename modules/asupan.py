
"""
✘ **Bantuan Untuk Asupan**

๏ **Perintah:** `asupan`
◉ **Keterangan:** Coba sendiri

๏ **Perintah:** `bokep`
◉ **Keterangan:** Coba sendiri

๏ **Perintah:** `ayang`
◉ **Keterangan:** Coba sendiri

๏ **Perintah:** `ppcp`
◉ **Keterangan:** Coba sendiri

๏ **Perintah:** `ppcp2`
◉ **Keterangan:** Coba sendiri

๏ **Perintah:** `anime`
◉ **Keterangan:** Coba sendiri

๏ **Perintah:** `anime2`
◉ **Keterangan:** Coba sendiri

๏ **Perintah:** `pap`
◉ **Keterangan:** Coba sendiri
"""

from secrets import choice

from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice, InputMessagesFilterPhotos

from . import 


@ayra_cmd(pattern="[Aa][s][u][p][a][n]$")
async def _(event):
    xx = await eor(event, "`Tunggu Sebentar...`")
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@punyakenkan", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(asupannya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan video asupan.**")


@ayra_cmd(pattern="[Bb][o][k][e][p]$")
async def _(event):
    if event.chat_id in NOSPAM_CHAT:
        return await eor(
            event, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    xx = await eor(event, "`Tunggu Sebentar...`")
    try:
        bokepnya = [
            bokep
            async for bokep in event.client.iter_messages(
                "@bahaninimah", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(bokepnya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan bokep.**")


@ayra_cmd(pattern="[Aa][y][a][n][g]$")
async def _(event):
    xx = await eor(event, "`Tunggu Sebentar...`")
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(ayangnya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan ayang.**")
        
@ayra_cmd(pattern="(ppcp|Ppcp)$")
async def _(event):
    xx = await eor(event, "`Tunggu Sebentar...`")
    try:
        ppcpnya = [
            ppcp
            async for ppcp in event.client.iter_messages(
                "@ppcpcilik", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(ppcpnya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan ppcp.**")

@ayra_cmd(pattern="(Ppcp2|ppcp2)$")
async def _(event):
    xx = await eor(event, "`Tunggu Sebentar...`")
    try:
        ajgg = [
            gg
            async for gg in event.client.iter_messages(
                "@mentahanppcp", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(ajgg), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan ppcp2.**")

@ayra_cmd(pattern="(Anime|anime)$")
async def _(event):
    xx = await eor(event, "`Tunggu Sebentar...`")
    try:
        nimek = [
            nime
            async for nime in event.client.iter_messages(
                "@animehikarixa", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(nimek), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan anime.**")

@ayra_cmd(pattern="(anime2|Anime2)$")
async def _(event):
    xx = await eor(event, "`Tunggu Sebentar...`")
    try:
        nimekk = [
            nim
            async for nim in event.client.iter_messages(
                "@animehikarixa", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(nimekk), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan anime2.**")


@ayra_cmd(pattern="(pap|Pap)$")
async def _(event):
    xx = await eor(event, "`Tunggu Sebentar...`")
    try:
        papjing = [
            jinglu
            async for jinglu in event.client.iter_messages(
                "@mm_kyran", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(papjing), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan desahan cowo.**")

