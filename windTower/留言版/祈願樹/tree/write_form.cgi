print<<HTML;
<script>
function return_mess() {
	var d = document.f1;
	if (!d.username.value) {alert("�п�J�m�W"); d.username.focus(); return false;}
	if (!d.comment.value) {alert("�п�J�d��"); d.comment.focus(); return false;}
	opener.document.f1.username.value = d.username.value;
	opener.document.f1.comment.value = d.comment.value;
	opener.document.f1.job.value='write';
	opener.document.f1.target='_self';
	opener.document.f1.submit();
	window.close();
	return false;
}
</script>
<body onload='document.f1.username.focus();' topmargin="0" leftmargin="0" bgcolor="#FFFFFF">
<form name='f1' onsubmit=return(return_mess());>
<table border=0 cellSpacing=0 cellPadding=3 width='100%' height='100%'  align='center'><tr><td align=center class=t4d>
<table border='0' cellSpacing=0 cellPadding=0 width='100%' height='100%' align='center'  class=t4>
<tr><td  align=\"center\">��֤��e��40�Ӥ���r��</td></tr>
<tr>
<td align=\"center\">��֪�: <input name='username' maxlength=\"8\" size=12></td></tr>
<tr><td align=\"center\" >
<input type="text" name='comment' size="25" maxlength="40"  value=�мg�X�z���Ʊ�!></td></tr>
<tr><td align=\"center\"><input type='submit' value='���ڦ��u' class=bot>**<input type='reset' value='�|�L�@��' class=bot></tr>
</table>

</form>
</body></html>
<noscript><!--#echo banner=""--></noscript>
HTML

exit;