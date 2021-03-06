@client.command()
@commands.has_permissions(ban_members=True, kick_members=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("**Please select a member**")
        return
    await member.ban()
    await ctx.send(f"{member.mention} Was banned by {ctx.author.mention}, [{reason}]")
# This displays an error if the user doesn't have the required permmissions
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("**Nerd You Cant Ban People**")
