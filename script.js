function switchLanguage() {
    const currentLang = localStorage.getItem('language') || 'en';
    const newLang = currentLang === 'en' ? 'zh' : 'en';
    
    localStorage.setItem('language', newLang);
    updateUI(newLang);
    
    document.getElementById('lang-toggle').textContent = 
        newLang === 'en' ? '中文' : 'English';
}

function updateUI(lang) {
    fetch('resume.json')
        .then(response => response.json())
        .then(data => {
            const resume = data[lang];
            
            // 更新个人信息
            document.getElementById('name').textContent = resume.name;
            document.getElementById('location').textContent = resume.location;
            document.getElementById('email').textContent = resume.email;
            document.getElementById('phone').textContent = resume.phone;
            document.getElementById('github').textContent = resume.github;
            document.getElementById('linkedin').textContent = resume.linkedin;
            
            // 更新教育经历
            const eduList = document.getElementById('education-list');
            eduList.innerHTML = '';
            resume.education.forEach(edu => {
                eduList.innerHTML += `
                    <div class="experience-item">
                        <h3>${edu.institution}</h3>
                        <div class="date">${edu.date}</div>
                        <p><strong>${edu.degree}</strong></p>
                        <p>${edu.description}</p>
                    </div>
                `;
            });
            
            // 更新工作经历
            const expList = document.getElementById('experience-list');
            expList.innerHTML = '';
            resume.experience.forEach(exp => {
                expList.innerHTML += `
                    <div class="experience-item">
                        <h3>${exp.company}</h3>
                        <div class="date">${exp.date}</div>
                        <p><strong>${exp.position}</strong></p>
                        <p>${exp.description}</p>
                    </div>
                `;
            });
        })
        .catch(error => console.error('Error loading resume:', error));
}

document.addEventListener('DOMContentLoaded', () => {
    const lang = localStorage.getItem('language') || 'en';
    updateUI(lang);
    
    document.getElementById('lang-toggle').addEventListener('click', switchLanguage);
    document.getElementById('lang-toggle').textContent = lang === 'en' ? '中文' : 'English';
});