import { useMemo } from 'react';
import { PageHeader } from '../components/PageHeader';
import { useArticlesStore } from '../store';

const Home = () => {
  const { articles, featuredCategory, setFeaturedCategory } = useArticlesStore();
  const featuredArticles = useMemo(
    () => articles.filter((article) => article.category === featuredCategory),
    [articles, featuredCategory],
  );

  const categories = useMemo(() => Array.from(new Set(articles.map((a) => a.category))), [articles]);

  return (
    <section>
      <PageHeader
        title="Curate tomorrow's headlines"
        subtitle="Prototype the NewsKoo experience with curated story stacks and research timelines."
        actions={
          <div>
            <button type="button">Book a Demo</button>
            <button type="button" style={{ background: 'transparent', color: '#fcd34d', border: '1px solid #fcd34d' }}>
              Explore Docs
            </button>
          </div>
        }
      />

      <div style={{ marginTop: '2rem' }}>
        <h2>Featured focus</h2>
        <p>Spotlight a category to see what the newsroom is tracking in real time.</p>
        <div style={{ display: 'flex', gap: '0.75rem', marginTop: '1rem', flexWrap: 'wrap' }}>
          {categories.map((category) => (
            <button
              key={category}
              type="button"
              onClick={() => setFeaturedCategory(category)}
              style={{
                padding: '0.5rem 1rem',
                borderRadius: '999px',
                border: '1px solid rgba(255,255,255,0.2)',
                background: category === featuredCategory ? '#fcd34d' : 'transparent',
                color: category === featuredCategory ? '#1a1f2c' : '#f1f5f9',
                cursor: 'pointer',
              }}
            >
              {category}
            </button>
          ))}
        </div>
      </div>

      <div className="card-grid">
        {featuredArticles.map((article) => (
          <article key={article.id} className="card">
            <span className="badge">{article.category}</span>
            <h3>{article.title}</h3>
            <p>{article.excerpt}</p>
            <small>Published {new Date(article.publishedAt).toLocaleDateString()}</small>
          </article>
        ))}
      </div>

      <div className="timeline">
        <h3>Research timeline</h3>
        {[...featuredArticles].map((article, index) => (
          <div key={article.id} className="timeline-item">
            <time>{new Date(article.publishedAt).toLocaleDateString()}</time>
            <div>
              <p style={{ margin: 0, fontWeight: 600 }}>{article.title}</p>
              <p style={{ margin: '0.25rem 0 0', color: 'rgba(255,255,255,0.7)' }}>
                Milestone #{index + 1}: stakeholder interviews &amp; prototype briefs.
              </p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Home;
