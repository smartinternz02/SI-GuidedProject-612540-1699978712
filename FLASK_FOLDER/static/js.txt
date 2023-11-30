<script>
    function showContent(section) {
        document.getElementById('covid19Content').style.display = 'none';
        document.getElementById('aboutContent').style.display = 'none';
        document.getElementById('precautionsContent').style.display = 'none';
        document.getElementById('vaccinationsContent').style.display = 'none';
        document.getElementById('testContent').style.display = 'none';

        document.getElementById(section + 'Content').style.display = 'block';
    }
</script>
